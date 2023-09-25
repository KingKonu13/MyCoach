import os
from embedchain import App
from dotenv import load_dotenv
from string import Template


load_dotenv()

# Create a bot instance of the coach 
os.environ["OPENAI_API_KEY"] = "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"

coach_bot = App()

coach_bot_chat_template = Template(
    """
        You are a career coach for college students. Make sure you are friendly and clear, keep in mind that you are talking to college students)

        Use the following information about Boston Consulting Group to respond to
        the human's query acting as a career coach.
        Context: $context

        Keep the response brief. If you don't know the answer, just say that you don't know, don't try to make up an answer.

        Human: $query
        Career Coach:""")
        
coach_bot.add("https://careers.bcg.com/on-campus/university-of-pennsylvania")
coach_bot.add("https://careers.bcg.com/blogarticle/10-frequently-asked-questions-bcg-internships")
coach_bot.add("https://docs.google.com/document/d/e/2PACX-1vQjnnACx6FEa9RkyXzQLxTMS88X17d4I1IGq6md5B6mOAKTMGbujj6uUz8QRMiPs7jjUIcvri0zs5eY/pub")
coach_bot.add("https://www.bcg.com")
coach_bot.add("https://docs.google.com/document/d/e/2PACX-1vTJk9u5VfKHUAzQNBLLLOVL_y9g1x9BWRFzD83XU5wXBpTOYidbMUkpXS2tFpYK7NbbIgj432Uo3cXa/pub")
coach_bot.add("https://www.youtube.com/watch?v=1TlgIYMLork")
coach_bot.add("https://www.youtube.com/watch?v=gTi8qAVGeCo")
coach_bot.add("https://www.youtube.com/watch?v=YmcbMGt0e_Q")
coach_bot.add("https://www.youtube.com/watch?v=ZAEyoKQOctU")
coach_bot.add("https://www.youtube.com/watch?v=uhR9Lq3fWM8")
coach_bot.add("https://acrobat.adobe.com/link/review?uri=urn:aaid:scds:US:404c9a85-1952-3e4e-a3d3-ab29ba8e9eb2")

response = coach_bot.query("Help me practice for a casing interveiw at BCG")
print(response)