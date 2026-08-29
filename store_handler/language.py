"""
Multi-language Support Module
Support for English, Hindi, Nepali, Arabic
"""

class LanguageSupport:
    """Handle multi-language support"""
    
    SUPPORTED_LANGUAGES = ['english', 'hindi', 'nepali', 'arabic']
    
    def __init__(self, default_language: str = 'english'):
        self.default_language = default_language
        self.translations = {}
    
    def add_translation(self, key: str, language: str, text: str) -> bool:
        """Add translation for a key"""
        if language not in self.SUPPORTED_LANGUAGES:
            return False
        
        if key not in self.translations:
            self.translations[key] = {}
        
        self.translations[key][language] = text
        return True
    
    def get_text(self, key: str, language: str = None) -> str:
        """Get translated text"""
        if language is None:
            language = self.default_language
        
        if language not in self.SUPPORTED_LANGUAGES:
            return ""
        
        if key not in self.translations:
            return key
        
        if language not in self.translations[key]:
            return self.translations[key].get(self.default_language, key)
        
        return self.translations[key][language]
    
    def set_default_language(self, language: str) -> bool:
        """Set default language"""
        if language not in self.SUPPORTED_LANGUAGES:
            return False
        
        self.default_language = language
        return True
    
    def is_language_supported(self, language: str) -> bool:
        """Check if language is supported"""
        return language.lower() in self.SUPPORTED_LANGUAGES
