# Sentiment Analyzer 🎭

A Python tool that reads any text and instantly tells you 
whether it is positive, negative or neutral.

## The Problem
Understanding the emotion behind text is hard for machines. 
This tool uses machine learning to analyze human language 
and detect sentiment automatically.

## What it does
- Takes any sentence as input
- Analyzes the emotion behind the words
- Returns Positive, Negative or Neutral result
- Shows a detailed score breakdown
- Runs interactively — type anything and get instant results

## Example output
Enter text: I love programming, it is amazing!
Sentiment: Positive 😊
Score: {'neg': 0.0, 'neu': 0.266, 'pos': 0.734, 'compound': 0.8516}
Enter text: This is the worst experience ever.
Sentiment: Negative 😞
Score: {'neg': 0.451, 'neu': 0.549, 'pos': 0.0, 'compound': -0.6249}
