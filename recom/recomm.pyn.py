import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from collections import defaultdict

class RecommendationSystem1:
    def __init__(self):
        self.moviePreferences = defaultdict(list)
        self.bookPreferences = defaultdict(list)
        self.productPreferences = defaultdict(list)
        self.userProfiles = {}
        
        self.moviePreferences["action"] = ["Movie1", "Movie2", "Movie3"]
        self.moviePreferences["comedy"] = ["Movie4", "Movie5", "Movie6"]
        self.moviePreferences["drama"] = ["Movie7", "Movie8", "Movie9"]
        self.bookPreferences["fantasy"] = ["Book1", "Book2", "Book3"]
        self.bookPreferences["mystery"] = ["Book4", "Book5", "Book6"]
        self.bookPreferences["romance"] = ["Book7", "Book8", "Book9"]
        self.productPreferences["electronics"] = ["Product1", "Product2", "Product3"]
        self.productPreferences["clothing"] = ["Product4", "Product5", "Product6"]
        self.productPreferences["home"] = ["Product7", "Product8", "Product9"]
        
        self.root = tk.Tk()
        self.root.title("Advanced Recommendation System")
        
        self.titleLabel = ttk.Label(self.root, text="Welcome to the Recommendation System")
        self.titleLabel.pack()
        
        self.userLabel = ttk.Label(self.root, text="Select User:")
        self.userLabel.pack()
        
        self.userComboBox = ttk.Combobox(self.root, values=["User1", "User2", "User3"])
        self.userComboBox.pack()
        
        self.preferenceTypeLabel = ttk.Label(self.root, text="Select Preference Type:")
        self.preferenceTypeLabel.pack()
        
        self.preferenceTypeComboBox = ttk.Combobox(self.root, values=["Movies", "Books", "Products"])
        self.preferenceTypeComboBox.pack()
        
        self.preferenceLabel = ttk.Label(self.root, text="Select Preference:")
        self.preferenceLabel.pack()
        
        self.preferenceComboBox = ttk.Combobox(self.root)
        self.preferenceComboBox.pack()
        
        self.setPreferenceButton = ttk.Button(self.root, text="Set User Preference", command=self.set_preference)
        self.setPreferenceButton.pack()
        
        self.getRecommendationsButton = ttk.Button(self.root, text="Get Recommendations", command=self.get_recommendations)
        self.getRecommendationsButton.pack()
        
        self.recommendationsLabel = ttk.Label(self.root)
        self.recommendationsLabel.pack()
        
        self.preferenceTypeComboBox.bind("<<ComboboxSelected>>", self.update_preference_combobox)
        
    def update_preference_combobox(self, event):
        preferenceType = self.preferenceTypeComboBox.get().lower()
        if preferenceType == "movies":
            self.preferenceComboBox["values"] = list(self.moviePreferences.keys())
        elif preferenceType == "books":
            self.preferenceComboBox["values"] = list(self.bookPreferences.keys())
        elif preferenceType == "products":
            self.preferenceComboBox["values"] = list(self.productPreferences.keys())
            
    def set_preference(self):
        userName = self.userComboBox.get()
        preferenceType = self.preferenceTypeComboBox.get().lower()
        preference = self.preferenceComboBox.get().lower()
        
        userProfile = self.userProfiles.setdefault(userName, UserProfile(userName))
        userProfile.set_preference_type(preferenceType)
        userProfile.set_preference(preference)
        
        messagebox.showinfo("Success", "User preference set successfully.")
        
    def get_recommendations(self):
        userName = self.userComboBox.get()
        userProfile = self.userProfiles.get(userName)
        
        if userProfile:
            preferenceType = userProfile.get_preference_type()
            userPreference = userProfile.get_preference()
            
            preferencesMap = None
            if preferenceType == "movies":
                preferencesMap = self.moviePreferences
            elif preferenceType == "books":
                preferencesMap = self.bookPreferences
            elif preferenceType == "products":
                preferencesMap = self.productPreferences
                
            if preferencesMap:
                recommendations = preferencesMap.get(userPreference)
                self.recommendationsLabel["text"] = f"Recommended {userPreference} {preferenceType}: {', '.join(recommendations)}"
            else:
                self.recommendationsLabel["text"] = "Invalid preference type."
        else:
            self.recommendationsLabel["text"] = "User not found. Set user preference first."
        
    def run(self):
        self.root.mainloop()

class UserProfile:
    def __init__(self, userName):
        self.userName = userName
        self.preferenceType = None
        self.preference = None
        
    def get_preference_type(self):
        return self.preferenceType
    
    def set_preference_type(self, preferenceType):
        self.preferenceType = preferenceType
        
    def get_preference(self):
        return self.preference
    
    def set_preference(self, preference):
        self.preference = preference

if __name__ == "__main__":
    recommendation_system = RecommendationSystem1()
    recommendation_system.run()


