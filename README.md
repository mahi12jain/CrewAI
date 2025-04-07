# CrewAI YouTube Blog Generator

A powerful tool that uses AI agents to generate blog content from YouTube videos. This project leverages CrewAI to create a workflow of specialized agents that research, extract, and transform YouTube video content into engaging blog posts.

## Overview

This application uses a team of AI agents to:
1. Research and analyze YouTube videos on specified topics
2. Extract key information and insights from video transcripts
3. Generate well-structured blog content based on the video material

The system specifically targets AI, Data Science, Machine Learning, Deep Learning, and GenAI content from designated YouTube channels.

## Features

- **YouTube Channel Integration**: Automatically searches and extracts content from specified YouTube channels
- **Intelligent Research**: Uses specialized agents to research and understand video content
- **Content Generation**: Transforms video insights into well-structured blog posts
- **Topic Customization**: Easily specify topics of interest for content generation
- **File Output**: Automatically saves blog content to markdown files

## Prerequisites

- Python 3.8+
- OpenAI API key (or other compatible LLM provider)
- Hugging Face account (for embeddings)
- YouTube Data API key (for channel access)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/crewai-youtube-blog.git
cd crewai-youtube-blog
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your API keys:
```
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
YOUTUBE_API_KEY=your_youtube_api_key
```

## Project Structure

```
├── agents.py           # Defines CrewAI agents (blog_researcher, blog_writer)
├── task.py             # Defines tasks for the agents
├── tools.py            # YouTube search and analysis tools
├── crew.py             # Main execution script
├── .env                # Environment variables (API keys)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## Usage

1. Run the main script with your desired topic:
```bash
python main.py
```

2. The script will:
   - Search for videos on the specified topic from the configured YouTube channel
   - Extract and analyze the video content
   - Generate a blog post based on the video information
   - Save the blog post to a markdown file (`new-blog-post.md`)

3. You can customize the topic in the main script:
```python
result = crew.kickoff(inputs={'topic': 'Your Custom Topic Here'})
```

## Customizing Agents

The project contains two primary agents:

### Blog Researcher
Responsible for finding and analyzing YouTube video content:
```python
blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verbose=True,
    memory=True,
    backstory="Expert in understanding videos in AI Data Science, Machine Learning And GEN AI and providing suggestion",
    tools=[yt_tool],
    allow_delegation=True
)
```

### Blog Writer
Transforms research into engaging blog content:
```python
blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory="With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner.",
    tools=[yt_tool],
    allow_delegation=False
)
```

## Customizing YouTube Channel

Change the YouTube channel by modifying the `yt_tool` definition in `tools.py`:

```python
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="@YourPreferredChannel",
    embedder=hf_model,
)
```

## Requirements

- crewai
- dotenv
- sentence-transformers
- crewai-tools
- embedchain
- langchain
