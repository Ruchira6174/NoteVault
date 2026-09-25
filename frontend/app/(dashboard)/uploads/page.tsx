import type { Metadata } from 'next';
import UploadDropzone from '@/components/upload/upload-dropzone';
import MetadataForm from '@/components/upload/metadata-form';
import VisibilitySelector from '@/components/upload/visibility-selector';
import PricingCard from '@/components/upload/pricing-card';
import UploadProgress from '@/components/upload/upload-progress';
import TagSelector from '@/components/upload/tag-selector';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { useState } from 'react';

export const metadata: Metadata = {
  title: 'Upload Resource',
};

export default function UploadResourcePage() {
  const [step, setStep] = useState(0);
  const steps = [
    'Upload files',
    'Add metadata',
    'Visibility & pricing',
    'AI verification',
    'Publish',
  ];

  return (
    <div className="space-y-8 p-4">
      <UploadProgress currentStep={step} steps={steps} />
      {step === 0 && (
        <Card>
          <CardHeader>
            <CardTitle>Step 1 – Upload Files</CardTitle>
          </CardHeader>
          <CardContent>
            <UploadDropzone onSuccess={() => setStep(1)} />
          </CardContent>
        </Card>
      )}
      {step === 1 && (
        <Card>
          <CardHeader>
            <CardTitle>Step 2 – Resource Information</CardTitle>
          </CardHeader>
          <CardContent>
            <MetadataForm onSubmit={() => setStep(2)} />
          </CardContent>
        </Card>
      )}
      {step === 2 && (
        <div className="grid gap-6 md:grid-cols-2">
          <Card>
            <CardHeader>
              <CardTitle>Visibility</CardTitle>
            </CardHeader>
            <CardContent>
              <VisibilitySelector onSelect={() => setStep(3)} />
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Pricing</CardTitle>
            </CardHeader>
            <CardContent>
              <PricingCard onSelect={() => setStep(3)} />
            </CardContent>
          </Card>
        </div>
      )}
      {step === 3 && (
        <Card>
          <CardHeader>
            <CardTitle>AI Verification (preview)</CardTitle>
          </CardHeader>
          <CardContent>
            {/* Placeholder AI report */}
            <p className="text-sm text-slate-600 dark:text-slate-400">AI verification will appear here after upload.</p>
            <button
              className="mt-4 rounded-xl bg-blue-600 px-4 py-2 text-white transition-colors hover:bg-blue-700"
              onClick={() => setStep(4)}
            >
              Publish Resource
            </button>
          </CardContent>
        </Card>
      )}
      {step === 4 && (
        <Card>
          <CardHeader>
            <CardTitle>Success</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-green-600">Your resource has been uploaded and is now live.</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
