# Multilingual Poetry Bot

A Streamlit application that generates customized poetry in multiple languages using OpenAI's language models through the LangChain framework.

## Features

- **Multilingual Support**: Generate poetry in English and Tamil
- **Complexity Levels**: Choose between Simple and Advanced poetry styles
- **Customization Options**: 
  - Define the main theme of your poem
  - Add optional personal details or hints to personalize the poetry
- **OpenAI Integration**: Leverages OpenAI's powerful language models for high-quality poetry generation
- **Intuitive Interface**: Simple Streamlit UI for easy interaction

## Screenshot

![Poetry Bot Interface](path/to/screenshot.png)

## Requirements

- Python 3.7+
- Streamlit
- LangChain
- OpenAI API key

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/multilingual-poetry-bot.git
   cd multilingual-poetry-bot
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.streamlit/secrets.toml` file with your API key:
     ```toml
     OPENAI_API_KEY = "your-openai-api-key-here"
     ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Select your preferences:
   - Choose the complexity level (Simple or Advanced)
   - Select the language (English or Tamil)
   - Enter a main theme for your poem
   - Optionally add personal details or hints

3. Click "Generate Poetry" to create your customized poem

## How It Works

The application uses LangChain to interface with OpenAI's language models. Based on your selected language and complexity level, it constructs a prompt template that guides the AI to generate appropriate poetry.

For English poems:
- Simple: Creates heartfelt 4-line poems with simple language and rhyming
- Advanced: Composes more sophisticated poems with metaphors and lyrical flow

For Tamil poems:
- Simple: Generates 4-line poems with basic Tamil vocabulary and rhythm
- Advanced: Creates poems that incorporate traditional Tamil poetic elements

## Customization

You can extend this application by:
- Adding more languages
- Creating additional complexity levels
- Implementing different poetry styles or formats

## Security Note

This application requires an OpenAI API key. Please keep your API key secure and never commit it directly to your repository. Use environment variables or Streamlit's secrets management as shown in the installation instructions.

## License

[MIT License](LICENSE)
