import type { Metadata } from 'next';
import ProfileHeader from '@/components/profile/profile-header';
import ProfileCard from '@/components/profile/profile-card';
import AcademicInfo from '@/components/profile/academic-info';
import CreatorBadge from '@/components/profile/creator-badge';
import { Card, CardContent } from '@/components/ui/card';

export const metadata: Metadata = {
  title: 'My Profile',
};

export default function ProfilePage() {
  // Mock data
  const user = {
    name: 'Ruchira Pophli',
    username: 'ruchira123',
    avatarUrl: '/placeholder-avatar.png',
    verified: true,
    college: 'ABC College of Engineering',
    university: 'XYZ University',
    course: 'B.Tech',
    branch: 'Computer Science',
    semester: 6,
    bio: 'Passionate about algorithms and open-source.',
    stats: {
      published: 4,
      sales: 1200,
      rating: 4.8,
      downloads: 350,
    },
  };
  return (
    <div className="space-y-6 p-4">
      <ProfileHeader avatarUrl={user.avatarUrl} name={user.name} username={user.username} verified={user.verified} />
      <CreatorBadge />
      <Card>
        <CardContent className="grid gap-4 md:grid-cols-2">
          <ProfileCard label="College" value={user.college} />
          <ProfileCard label="University" value={user.university} />
          <ProfileCard label="Course" value={user.course} />
          <ProfileCard label="Branch" value={user.branch} />
          <ProfileCard label="Semester" value={String(user.semester)} />
          <ProfileCard label="Bio" value={user.bio} />
        </CardContent>
      </Card>
      <AcademicInfo stats={user.stats} />
    </div>
  );
}
