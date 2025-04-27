from data.connection import db
from data.models.models import Profile
from sqlalchemy import text

class ProfileService:
    def __init__(self) -> None:
        pass

    def create_profile(self, first_name, last_name, age):
        profile = Profile(first_name=first_name, last_name=last_name, age=age)
        obj = db.session.add(profile)
        obj = db.session.commit()

    def get_profile_by_name(self, first_name):
        return Profile.query.filter_by(first_name=first_name).first()

    def get_profile_by_id(self, profile_id):        
        profile = Profile.query.get(profile_id)
        #profile = Profile.query.filter_by(id=profile_id).first()
        return profile.to_dict()
        '''
        return {'id': profile.id, 
                'first_name': profile.first_name, 
                'last_name': profile.last_name, 
                'age': profile.age} if profile else {}
        '''

    def delete_profile_by_id(self, profile_id):
        profile = Profile.query.get(profile_id)
        if profile:
            db.session.delete(profile)
            db.session.commit()
            return True
        else:
            return True


    def list_profile(self):
        profiles = Profile.query.all()

        return [{'id': x.id,
                 'first_name': x.first_name,
                 'age': x.age
                } for x in profiles]


    def get_profile_by_query(self, profile_id):
        result = db.session.execute(text("SELECT * FROM profile"))
        profile = Profile(result.fetchone())
        return profile.to_dict()        

        query = f"SELECT * FROM Profile WHERE id = {profile_id}"  # ❌ Vulnerable to SQL Injection
        query = text("SELECT * FROM Profile WHERE id = :id")  # ✅ Use :id placeholder
        result = db.session.execute(query, {"id": profile_id})  # ✅ Bind parameter safely
        profile = Profile(result.fetchone())
        return profile.to_dict()        

        '''
        🔥 Final Checklist to Prevent SQL Injection
        - Use SQLAlchemy ORM (filter_by())      -> Automatically prevents SQL injection
        - Use parameterized queries (:param)    -> Prevents direct SQL execution
        - Validate user input	                -> Ensures only expected data is processed
        - Restrict special characters	        -> Stops SQL-breaking inputs
        - Implement role-based access (RBAC)    -> Limits sensitive actions to admins
        - Use Web Application Firewalls (WAF)   -> Blocks attacks before they reach the server
        - Disable Flask Debug Mode	            -> Prevents leaking database details
        '''


