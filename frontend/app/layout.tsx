import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { AppProvider } from "@/providers/AppProvider";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "NoteVault AI",
  description: "AI-powered study material marketplace",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {/* TODO: Add proper layout structure */}
        <AppProvider>{children}</AppProvider>
      </body>
    </html>
  );
}
