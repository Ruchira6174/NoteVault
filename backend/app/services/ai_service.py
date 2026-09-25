from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime, timezone
from fastapi import HTTPException
from app.models.resource import Resource
from app.models.ai_report import AIReport
from app.ai import (
    ocr, embeddings, vector_store, rag_pipeline, verifier,
    fact_checker, plagiarism, syllabus_mapper, summarizer,
    quiz_generator, ai_score
)

class AIService:
    @staticmethod
    def verify_resource(db: Session, resource_id: UUID) -> AIReport:
        """Orchestrate the complete AI verification pipeline."""
        resource = db.query(Resource).filter(Resource.id == resource_id).first()
        if not resource:
            raise HTTPException(status_code=404, detail="Resource not found")
            
        # 1. Load file
        file_path = "mock_file_path.pdf" # TODO: Get from resource.files
        
        # 2 & 3. OCR and Clean text
        text = ocr.extract_text(file_path)
        
        # 4. Chunk
        chunks = rag_pipeline.load_resource_chunks(text)
        
        # 5 & 6. Embed and Store vectors
        embedded_chunks = embeddings.batch_embeddings(chunks)
        vector_store.vector_store.add_documents(resource_id, chunks, embedded_chunks)
        
        # 7. Verify
        context = rag_pipeline.build_context("verification query", resource_id)
        verification_results = verifier.verify_resource(text, context)
        fact_results = fact_checker.check_facts(text, context)
        plagiarism_results = plagiarism.estimate_originality(text)
        syllabus_results = syllabus_mapper.map_syllabus(text, resource.university or "", resource.subject or "")
        
        # 8. Generate summary
        summary_results = summarizer.generate_summary(text)
        
        # 9. Generate quiz
        quizzes = quiz_generator.generate_mcqs(text)
        
        # 10. Compute final scores
        final_scores = ai_score.calculate_final_score({
            "accuracy": verification_results["factual_accuracy"],
            "originality": plagiarism_results["originality_score"],
            "readability": verification_results["readability"],
            "syllabus": syllabus_results["coverage_percentage"]
        })
        
        # 11. Save AIReport
        ai_report = db.query(AIReport).filter(AIReport.resource_id == resource_id).first()
        if not ai_report:
            ai_report = AIReport(resource_id=resource_id)
            db.add(ai_report)
            
        ai_report.accuracy_score = final_scores["accuracy_score"]
        ai_report.originality_score = final_scores["originality_score"]
        ai_report.readability_score = final_scores["readability_score"]
        ai_report.syllabus_coverage = final_scores["syllabus_coverage"]
        ai_report.plagiarism_percentage = plagiarism_results["plagiarism_percentage"]
        ai_report.ai_summary = summary_results["ai_summary"]
        ai_report.generated_quiz_count = len(quizzes)
        ai_report.verified_at = datetime.now(timezone.utc)
        
        db.commit()
        db.refresh(ai_report)
        
        return ai_report

    @staticmethod
    def get_ai_report(db: Session, resource_id: UUID) -> AIReport:
        ai_report = db.query(AIReport).filter(AIReport.resource_id == resource_id).first()
        if not ai_report:
            raise HTTPException(status_code=404, detail="AI report not found")
        return ai_report

    @staticmethod
    def get_quiz(db: Session, resource_id: UUID) -> list:
        # TODO: Retrieve generated quizzes (e.g., from a separate DB table if stored)
        # Returning mock quiz data
        return quiz_generator.generate_mcqs("mock text")
