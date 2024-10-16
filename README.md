# AOne
All-in-one AI assistant to help me with my everyday tasks

1. Expense tracking with AI
    1. Input: text, picture (receipt), ?voice
        1. OCR: EasyOCR
            1. 1013: The results of directly applying EasyOCR are poor. Try to preprocess the image or use LMM.
            2. 1015: Using Llama3.2 with Cloudflare Workers AI but having trouble uploading images.
            3. 1016: Deleted easyOCR, replace it with Google AI
        2. OCR: Google AI
            1. 1016: The output is very great. Test it with more images.

    2. Recognize item names, categorize items, and pinpoint purchase locations for
    3. Save information to SQL database
    4. Output
        1. Expenses over a period of time
        2. Time-based and location-based price analysis
        3. ?Graph
        4. ?Recommendations for better spending habits

