from feed.models import Post


class SearchEngine:

    def search(self, preference):
        posts = Post.posts.filter(is_job_offer=True)

        if(preference.job_type is not None):
            posts = filter(lambda post: post.prefernces.job_type == preference.job_type, posts)

        if(preference.location is not None):
            posts = filter(lambda post: post.prefernces.location == preference.location, posts)

        posts = filter(lambda post: post.prefernces.years_of_experience == preference.years_of_experience, posts)
        posts = filter(lambda post: post.prefernces.work_schedule == preference.work_schedule, posts)

        return posts
