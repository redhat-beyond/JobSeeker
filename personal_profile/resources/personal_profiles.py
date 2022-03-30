from django.db import models
PERSONAL_PROFILES = [
    [
        'Microsoft',
        'Bil Gates',
        'Im a co-founder of microsoft, and have been the richest guy in the world for a while...',
        models.DateField(1955, 10, 28),
        'personal_profile/static/personal_profile/images/profile_pics/billgates.jpg',
        'personal_profile/static/personal_profile/images/resumes/billgates_resume.jpg',
    ],
    [
        'Apple',
        'Tim Cook',
        'Im the CEO of Apple, and honestly Im just the guy everyone calls Steve Jobs',
        models.DateField(1960, 11, 1),
        'personal_profile/static/personal_profile/images/profile_pics/timcook.jpg',
        'personal_profile/static/personal_profile/images/resumes/billgates_resume.jpg',
    ],
    [
        'Blank',
        'Jane Doe',
        'Web page designing is my greates passion, django specialist and a people person',
        models.DateField(1995, 12, 10),
        'personal_profile/static/personal_profile/images/profile_pics/jane.jpg',
        'personal_profile/static/personal_profile/images/resumes/billgates_resume.jpg',
    ]
]