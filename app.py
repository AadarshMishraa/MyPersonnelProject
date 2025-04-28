# app.py
from flask import Flask, request, jsonify, render_template
from content_suggester import suggest_content
from script_generator import generate_script
from trending import get_google_trends

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    # Dummy logic for extracting details
    product_type = "tech"          # Example value
    platform = "YouTube"           # Example value
    trending_keyword = "latest gadget"  # Dummy trending keyword

    # Get trending value using pytrends for the keyword
    trend_value = get_google_trends(trending_keyword)
    trending_keywords = [trending_keyword]  # You can refine this

    # Get content suggestions
    suggestions = suggest_content(product_type, trending_keywords, platform)

    # Create script prompt and generate script using OpenAI API
    script_prompt = (f"Generate a creative ad script for a {product_type} product on {platform} "
                     f"focusing on trends like {', '.join(trending_keywords)}. Suggestion: {suggestions[0]}")
    generated_script = generate_script(script_prompt)

    response = {
        "suggestions": suggestions,
        "script": generated_script
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
