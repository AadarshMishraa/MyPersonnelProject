# content_suggester.py
def suggest_content(product_type, trending_keywords, platform):
    suggestions = []

    if product_type.lower() == "fashion":
        if platform.lower() == "instagram":
            suggestions.append("High-quality visuals and stories showcasing style trends.")
        elif platform.lower() == "youtube":
            suggestions.append("Lookbook videos, style tips, behind-the-scenes at fashion shows.")
    elif product_type.lower() == "tech":
        if platform.lower() == "youtube":
            suggestions.append("Product reviews, unboxings, and tech explainer videos.")
        elif platform.lower() == "facebook":
            suggestions.append("How-to guides, live Q&A sessions.")
    else:
        suggestions.append("Interactive posts aligning with current trends: " + ", ".join(trending_keywords))
    
    return suggestions
 