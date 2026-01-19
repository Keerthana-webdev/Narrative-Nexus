def load_css():
    return """
<style>

    /*FONT*/
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    /*GENERAL PAGE STYLING*/
    .main {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #e0e0e0;
        font-family: 'Poppins', sans-serif;
    }

    .page-title {
        text-align: center;
        color: #ffffff;
        font-size: 48px;
        margin-bottom: 5px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
    }

    .page-subtitle {
        text-align: center;
        color: #a39fc9;
        font-size: 22px;
        margin-bottom: 35px;
        font-weight: 400;
    }

    /*CARD SECTIONS (Glassmorphism)*/
    .card-section {
        background: rgba(255, 255, 255, 0.08);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    .center {
        text-align: center;
    }

    .section-title {
        font-size: 24px;
        color: #e6d4ff;
        font-weight: 600;
        margin-bottom: 15px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        padding-bottom: 10px;
    }

    /*TEXT BOXES*/
    .text-box {
        background: rgba(0, 0, 0, 0.25);
        color: #f0f0f0;
        padding: 15px;
        height: 280px;
        overflow-y: auto;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        font-size: 14px;
        font-family: 'monospace';
    }

    .text-box-title {
        font-size: 18px;
        margin-bottom: 10px;
        color: #e6d4ff;
        font-weight: 600;
    }

    /*Scrollbar*/
    .text-box::-webkit-scrollbar { width: 8px; }
    .text-box::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 10px;
    }
    .text-box::-webkit-scrollbar-thumb {
        background-color: #888;
        border-radius: 10px;
        border: 2px solid transparent;
        background-clip: content-box;
    }
    .text-box::-webkit-scrollbar-thumb:hover {
        background-color: #555;
    }

    /*STAT CARDS*/
    .stat-card {
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .stat-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    }

    /*NEW UNIFIED COLOR THEME*/
    .blue  { background: linear-gradient(135deg,#00c6ff,#0072ff) !important; }
    .purple { background: linear-gradient(135deg,#7f00ff,#e100ff) !important; }

    .stat-number {
        font-size: 36px;
        font-weight: 700;
    }

    .stat-label {
        font-size: 14px;
        margin-top: 5px;
        font-weight: 400;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /*REDUCTION CARD*/
    .reduce-card {
        background: rgba(0, 0, 0, 0.2);
        padding: 15px;
        font-size: 18px;
        text-align: center;
        border-radius: 12px;
        border: 1px solid #8E2DE2;
        color: #f0f0f0;
        font-weight: 600;
    }

    /*FILE TITLE*/
    .file-title {
        background: rgba(0, 0, 0, 0.25);
        padding: 15px;
        border-radius: 12px;
        font-size: 20px;
        margin-top: 25px;
        margin-bottom: 10px;
        font-weight: 600;
        border-left: 5px solid #00c6ff;
    }

    /*BUTTON STYLING*/
    .stButton>button {
        background: linear-gradient(90deg, #6a11cb, #2575fc) !important;
        color: white;
        border: none;
        padding: 16px 25px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 700;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        filter: brightness(1.1);
    }

    /*INPUT FIELDS*/
    .stTextInput>div>div>input, 
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.08);
        color: white;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        font-size: 16px;
        transition: border-color 0.3s, box-shadow 0.3s;
    }

    .stTextInput>div>div>input:focus, 
    .stTextArea textarea:focus {
        border-color: #2575fc;
        box-shadow: 0 0 8px rgba(37, 117, 252, 0.5);
    }

</style>
"""
