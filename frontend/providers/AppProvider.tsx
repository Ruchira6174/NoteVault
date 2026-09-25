'use client';
import React from 'react';

// Global providers wrapper
export function AppProvider({ children }: { children: React.ReactNode }) {
  return (
    <>
      {/* TODO: Wrap with Redux/ReactQuery/ThemeProvider */}
      {children}
    </>
  );
}
