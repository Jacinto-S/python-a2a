"""
Setup script for python-a2a.

This setup script is maintained for backward compatibility.
For modern installations, please use pyproject.toml with pip or uv.
"""

from setuptools import setup, find_packages
import os

# Read the README file for the long description
this_directory = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = "A Python library for Google's Agent-to-Agent (A2A) protocol"

# This setup.py is maintained for backward compatibility
# For modern installations, please use pyproject.toml with pip or uv
setup(
    name="python_a2a",
    version="0.4.0",  # Updated version
    author="Manoj Desai",
    author_email="themanojdesai@gmail.com",
    description="A comprehensive Python library for Google's Agent-to-Agent (A2A) protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/themanojdesai/python-a2a",
    project_urls={
        "Bug Tracker": "https://github.com/themanojdesai/python-a2a/issues",
        "Documentation": "https://python-a2a.readthedocs.io",
        "Source Code": "https://github.com/themanojdesai/python-a2a",
    },
    packages=find_packages(),
    package_data={
        "python_a2a": ["py.typed"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="a2a, agent, ai, llm, interoperability, google, protocol, chatbot, openai, anthropic, claude, huggingface, mcp, model-context-protocol, aws-bedrock",
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.12.0",
            "black>=21.5b2",
            "flake8>=3.9.2",
            "mypy>=0.812",
            "responses>=0.13.3",
        ],
        "server": [
            "flask>=2.0.0",
            "aiohttp>=3.8.0",  # Added for streaming support
        ],
        "openai": [
            "openai>=1.0.0",
        ],
        "anthropic": [
            "anthropic>=0.3.0",
        ],
        "bedrock": [
            "boto3>=1.26.0",
            "botocore>=1.29.0",
        ],
        "mcp": [
            "httpx>=0.23.0",
            "fastapi>=0.95.0",
            "uvicorn>=0.21.0",
            "pydantic>=1.10.7",
        ],
        "all": [
            "flask>=2.0.0",
            "openai>=1.0.0",
            "anthropic>=0.3.0",
            "boto3>=1.26.0",
            "botocore>=1.29.0",
            "httpx>=0.23.0",
            "fastapi>=0.95.0",
            "uvicorn>=0.21.0",
            "pydantic>=1.10.7",
            "aiohttp>=3.8.0",  # Added for streaming support
        ],
    },
    entry_points={
        "console_scripts": [
            "a2a=python_a2a.cli:main",
        ],
    },
)