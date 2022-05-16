from feed.models import Post
import math


class SearchEngine:

    @staticmethod
    def search(preference):
        posts = Post.posts.filter(is_job_offer=True)

        if(preference.job_type is not None):
            posts = list(filter(lambda post: post.prefernces.job_type == preference.job_type, posts))

        if(preference.location is not None):
            posts.sort(key=lambda post: SearchEngine.distance(post.prefernces.location, preference.location))

        posts = list(filter(lambda post: post.prefernces.years_of_experience == preference.years_of_experience, posts))
        posts = list(filter(lambda post: post.prefernces.work_schedule == preference.work_schedule, posts))

        return posts

    # Calculate the distance between locations with the Haversine formula
    @staticmethod
    def distance(location1, location2):
        lat1 = location1.latitude
        lon1 = location1.longitude
        lat2 = location2.latitude
        lon2 = location2.longitude

        # distance between latitude and longitudes
        dLat = (lat2 - lat1) * math.pi / 180.0
        dLon = (lon2 - lon1) * math.pi / 180.0

        # convert to radians
        lat1 = (lat1) * math.pi / 180.0
        lat2 = (lat2) * math.pi / 180.0

        # apply formula
        a = (
            pow(math.sin(dLat / 2), 2) + pow(math.sin(dLon / 2), 2) * math.cos(lat1) * math.cos(lat2)
        )
        rad = 6371
        c = 2 * math.asin(math.sqrt(a))
        return rad * c
