# Kullanıcı sınıfı
class User:
    def __init__(self, user_id, username, universities, user_tags, experiences):
        self.user_id = user_id
        self.username = username
        self.universities = universities
        self.user_tags = user_tags
        self.experiences = experiences

# Kullanıcıları öneren fonksiyon
def recommend_users(target_user, all_users):
    # Önerilecek kullanıcıları saklamak için bir liste
    recommended_users = []

    for user in all_users:
        # Kendisiyle eşleşme yapmamak için kontrol
        if user.user_id == target_user.user_id:
            continue

        # Aynı üniversitelerden gelme
        common_universities = set(target_user.universities).intersection(user.universities)

        # Benzer işyerleri veya deneyimler
        common_experiences = set(target_user.experiences).intersection(user.experiences)

        # Ortak etiketler (ilgi alanları)
        common_tags = set(target_user.user_tags).intersection(user.user_tags)

        # En az biri benzerse önerilecek
        if common_universities or common_experiences or common_tags:
            recommendation_details = {
                "username": user.username,
                "common_universities": list(common_universities),
                "common_experiences": list(common_experiences),
                "common_tags": list(common_tags),
            }
            recommended_users.append(recommendation_details)

    return recommended_users

# Örnek kullanıcılar
users = [
    User(1, "alice", ["Harvard", "Stanford", "MIT"], ["Java", "Java Developer", "Backend Developer"], ["Data Scientist", "Analyst", "Researcher"]),
    User(2, "bob", ["MIT", "Caltech", "UC Berkeley"], ["Python", "Deep Learning", "Software Engineering"], ["Software Engineer", "Full Stack Developer", "Data Engineer"]),
    User(3, "charlie", ["Stanford", "Oxford", "Cambridge"], ["Data Analysis", "Machine Learning", "Big Data"], ["Researcher", "Data Analyst", "Statistician"]),
    User(4, "david", ["Harvard", "Stanford", "MIT"], ["Data Science", "Machine Learning", "Artificial Intelligence"], ["Data Scientist", "AI Researcher", "ML Engineer"]),
]

# Hedef kullanıcı ve önerileri almak
target_user = users[0]  # Alice
recommendations = recommend_users(target_user, users)

# Önerilen kullanıcıları yazdır
for recommendation in recommendations:
    print(f"Önerilen Kullanıcı: {recommendation['username']}, Ortak Üniversiteler: {recommendation['common_universities']}, Ortak Deneyimler: {recommendation['common_experiences']}, Ortak Etiketler: {recommendation['common_tags']}")
    