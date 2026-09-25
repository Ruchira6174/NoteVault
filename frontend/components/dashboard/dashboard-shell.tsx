import React from 'react';
import Sidebar from '@/components/dashboard/sidebar';
import TopBar from '@/components/dashboard/topbar';

interface DashboardShellProps {
  children: React.ReactNode;
}

export default function DashboardShell({ children }: DashboardShellProps) {
  return (
    <div className="flex min-h-screen bg-white dark:bg-slate-900">
      {/* Desktop sidebar */}
      <aside className="hidden md:flex md:w-64 md:flex-col md:border-r md:border-slate-200 dark:border-slate-700">
        <Sidebar />
      </aside>

      <div className="flex flex-1 flex-col">
        <TopBar />
        <main className="flex-1 overflow-y-auto p-4">
          {children}
        </main>
      </div>
    </div>
  );
}
