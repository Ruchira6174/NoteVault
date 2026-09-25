import type { Metadata } from 'next';
import QuickStats from '@/components/dashboard/quick-stats';
import RecentActivity from '@/components/dashboard/recent-activity';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

export const metadata: Metadata = {
  title: 'Dashboard Home',
};

// Mock data types
interface Stat {
  label: string;
  value: string | number;
}

const stats: Stat[] = [
  { label: 'Total Resources', value: 12 },
  { label: 'Purchased Notes', value: 5 },
  { label: 'Saved Bookmarks', value: 8 },
  { label: 'Avg AI Score', value: '87%' },
];

const recentActivities = [
  { id: 1, message: 'Uploaded OS Notes', time: '2h ago' },
  { id: 2, message: 'Purchase approved for "Data Structures"', time: '5h ago' },
  { id: 3, message: 'AI verification completed for "Algorithms"', time: '1d ago' },
];

export default function DashboardHome() {
  return (
    <div className="space-y-8 p-4">
      <Card>
        <CardHeader>
          <CardTitle>Welcome back!</CardTitle>
        </CardHeader>
        <CardContent className="text-sm text-slate-600 dark:text-slate-400">
          Here is a quick overview of your academic workspace.
        </CardContent>
      </Card>
      <QuickStats stats={stats} />
      <RecentActivity activities={recentActivities} />
    </div>
  );
}
