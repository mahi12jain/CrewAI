# from crewai_tools import YoutubeChannelSearchTool
# from embedchain.embedder import HuggingFaceEmbedder

# # Initialize the tool with a specific Youtube channel handle to target your search
# yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06', embedding_model=HuggingFaceEmbedder()  # Use Hugging Face Embedder
# )


from sentence_transformers import SentenceTransformer
from crewai_tools import YoutubeChannelSearchTool

# Initialize Hugging Face embedding model
hf_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Define the YouTube tool
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="@krishnaik06",
    embedder=hf_model,
)
