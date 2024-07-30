{
  "cells": [
    {
      "cell_type": "markdown",
      "id": "ca0d4e08-7701-44e9-9a9e-c7578a5ee258",
      "metadata": {
        "id": "ca0d4e08-7701-44e9-9a9e-c7578a5ee258"
      },
      "source": [
        "# Finance Copilot - LangGraph Architecture"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/genaiconference/AgenticAI_GenAIHack.git"
      ],
      "metadata": {
        "id": "7Z8BAwQNioN4",
        "collapsed": true,
        "outputId": "0cc62913-cf57-4fd3-b093-27f8667559af",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "id": "7Z8BAwQNioN4",
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'AgenticAI_GenAIHack'...\n",
            "remote: Enumerating objects: 119, done.\u001b[K\n",
            "remote: Counting objects: 100% (119/119), done.\u001b[K\n",
            "remote: Compressing objects: 100% (116/116), done.\u001b[K\n",
            "remote: Total 119 (delta 57), reused 0 (delta 0), pack-reused 0\u001b[K\n",
            "Receiving objects: 100% (119/119), 6.63 MiB | 3.72 MiB/s, done.\n",
            "Resolving deltas: 100% (57/57), done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt"
      ],
      "metadata": {
        "id": "X5Bw6hZviu1M",
        "collapsed": true,
        "outputId": "c05e40c9-8f67-4a07-d497-fa8f47399675",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "id": "X5Bw6hZviu1M",
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting beautifulsoup4==4.12.2 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 1))\n",
            "  Downloading beautifulsoup4-4.12.2-py3-none-any.whl.metadata (3.6 kB)\n",
            "Collecting chromadb==0.4.15 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading chromadb-0.4.15-py3-none-any.whl.metadata (7.2 kB)\n",
            "Collecting google-search-results==2.4.2 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 3))\n",
            "  Downloading google_search_results-2.4.2.tar.gz (18 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting langchain==0.2.9 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4))\n",
            "  Downloading langchain-0.2.9-py3-none-any.whl.metadata (6.9 kB)\n",
            "Collecting langchain-experimental==0.0.62 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 5))\n",
            "  Downloading langchain_experimental-0.0.62-py3-none-any.whl.metadata (1.5 kB)\n",
            "Collecting langchain-postgres==0.0.6 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 6))\n",
            "  Downloading langchain_postgres-0.0.6-py3-none-any.whl.metadata (3.7 kB)\n",
            "Collecting langchain-openai==0.1.7 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 7))\n",
            "  Downloading langchain_openai-0.1.7-py3-none-any.whl.metadata (2.5 kB)\n",
            "Collecting langgraph==0.0.55 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 8))\n",
            "  Downloading langgraph-0.0.55-py3-none-any.whl.metadata (23 kB)\n",
            "Collecting Markdown==3.5.2 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 9))\n",
            "  Downloading Markdown-3.5.2-py3-none-any.whl.metadata (7.0 kB)\n",
            "Collecting openai==1.30.5 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 10))\n",
            "  Downloading openai-1.30.5-py3-none-any.whl.metadata (21 kB)\n",
            "Collecting langchain-chroma==0.1.2 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 11))\n",
            "  Downloading langchain_chroma-0.1.2-py3-none-any.whl.metadata (1.3 kB)\n",
            "Collecting tavily-python==0.3.5 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 12))\n",
            "  Downloading tavily_python-0.3.5-py3-none-any.whl.metadata (11 kB)\n",
            "Collecting simple-colors==0.1.5 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 13))\n",
            "  Downloading simple_colors-0.1.5-py3-none-any.whl.metadata (1.5 kB)\n",
            "Collecting duckduckgo_search==4.4.3 (from -r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 14))\n",
            "  Downloading duckduckgo_search-4.4.3-py3-none-any.whl.metadata (19 kB)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4==4.12.2->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 1)) (2.5)\n",
            "Requirement already satisfied: requests>=2.28 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (2.31.0)\n",
            "Requirement already satisfied: pydantic>=1.9 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (2.8.2)\n",
            "Collecting chroma-hnswlib==0.7.3 (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading chroma_hnswlib-0.7.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (252 bytes)\n",
            "Collecting fastapi>=0.95.2 (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading fastapi-0.111.1-py3-none-any.whl.metadata (26 kB)\n",
            "Collecting uvicorn>=0.18.3 (from uvicorn[standard]>=0.18.3->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading uvicorn-0.30.3-py3-none-any.whl.metadata (6.5 kB)\n",
            "Collecting posthog>=2.4.0 (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading posthog-3.5.0-py2.py3-none-any.whl.metadata (2.0 kB)\n",
            "Requirement already satisfied: typing-extensions>=4.5.0 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (4.12.2)\n",
            "Collecting pulsar-client>=3.1.0 (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading pulsar_client-3.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.0 kB)\n",
            "Collecting onnxruntime>=1.14.1 (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading onnxruntime-1.18.1-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (4.3 kB)\n",
            "Collecting opentelemetry-api>=1.2.0 (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading opentelemetry_api-1.26.0-py3-none-any.whl.metadata (1.4 kB)\n",
            "Collecting opentelemetry-exporter-otlp-proto-grpc>=1.2.0 (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading opentelemetry_exporter_otlp_proto_grpc-1.26.0-py3-none-any.whl.metadata (2.3 kB)\n",
            "Collecting opentelemetry-sdk>=1.2.0 (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading opentelemetry_sdk-1.26.0-py3-none-any.whl.metadata (1.5 kB)\n",
            "Requirement already satisfied: tokenizers>=0.13.2 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (0.19.1)\n",
            "Collecting pypika>=0.48.9 (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading PyPika-0.48.9.tar.gz (67 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m67.3/67.3 kB\u001b[0m \u001b[31m3.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Installing build dependencies ... \u001b[?25l\u001b[?25hdone\n",
            "  Getting requirements to build wheel ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: tqdm>=4.65.0 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (4.66.4)\n",
            "Collecting overrides>=7.3.1 (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading overrides-7.7.0-py3-none-any.whl.metadata (5.8 kB)\n",
            "Requirement already satisfied: importlib-resources in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (6.4.0)\n",
            "Requirement already satisfied: grpcio>=1.58.0 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (1.64.1)\n",
            "Collecting bcrypt>=4.0.1 (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading bcrypt-4.2.0-cp39-abi3-manylinux_2_28_x86_64.whl.metadata (9.6 kB)\n",
            "Requirement already satisfied: typer>=0.9.0 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (0.12.3)\n",
            "Collecting kubernetes>=28.1.0 (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading kubernetes-30.1.0-py2.py3-none-any.whl.metadata (1.5 kB)\n",
            "Requirement already satisfied: tenacity>=8.2.3 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (8.5.0)\n",
            "Requirement already satisfied: numpy>=1.22.5 in /usr/local/lib/python3.10/dist-packages (from chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (1.26.4)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4)) (6.0.1)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.10/dist-packages (from langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4)) (2.0.31)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.10/dist-packages (from langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4)) (3.9.5)\n",
            "Requirement already satisfied: async-timeout<5.0.0,>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4)) (4.0.3)\n",
            "Collecting langchain-core<0.3.0,>=0.2.20 (from langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4))\n",
            "  Downloading langchain_core-0.2.24-py3-none-any.whl.metadata (6.2 kB)\n",
            "Collecting langchain-text-splitters<0.3.0,>=0.2.0 (from langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4))\n",
            "  Downloading langchain_text_splitters-0.2.2-py3-none-any.whl.metadata (2.1 kB)\n",
            "Collecting langsmith<0.2.0,>=0.1.17 (from langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4))\n",
            "  Downloading langsmith-0.1.93-py3-none-any.whl.metadata (13 kB)\n",
            "Collecting langchain-community<0.3.0,>=0.2.6 (from langchain-experimental==0.0.62->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 5))\n",
            "  Downloading langchain_community-0.2.10-py3-none-any.whl.metadata (2.7 kB)\n",
            "Collecting pgvector<0.3.0,>=0.2.5 (from langchain-postgres==0.0.6->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 6))\n",
            "  Downloading pgvector-0.2.5-py2.py3-none-any.whl.metadata (9.9 kB)\n",
            "Collecting psycopg<4,>=3 (from langchain-postgres==0.0.6->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 6))\n",
            "  Downloading psycopg-3.2.1-py3-none-any.whl.metadata (4.2 kB)\n",
            "Collecting psycopg-pool<4.0.0,>=3.2.1 (from langchain-postgres==0.0.6->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 6))\n",
            "  Downloading psycopg_pool-3.2.2-py3-none-any.whl.metadata (2.6 kB)\n",
            "Collecting tiktoken<1,>=0.7 (from langchain-openai==0.1.7->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 7))\n",
            "  Downloading tiktoken-0.7.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)\n",
            "Collecting uuid6<2025.0.0,>=2024.1.12 (from langgraph==0.0.55->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 8))\n",
            "  Downloading uuid6-2024.7.10-py3-none-any.whl.metadata (8.6 kB)\n",
            "Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.10/dist-packages (from openai==1.30.5->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 10)) (3.7.1)\n",
            "Requirement already satisfied: distro<2,>=1.7.0 in /usr/lib/python3/dist-packages (from openai==1.30.5->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 10)) (1.7.0)\n",
            "Collecting httpx<1,>=0.23.0 (from openai==1.30.5->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 10))\n",
            "  Downloading httpx-0.27.0-py3-none-any.whl.metadata (7.2 kB)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from openai==1.30.5->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 10)) (1.3.1)\n",
            "Requirement already satisfied: click>=8.1.7 in /usr/local/lib/python3.10/dist-packages (from duckduckgo_search==4.4.3->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 14)) (8.1.7)\n",
            "Collecting curl-cffi>=0.6.0b9 (from duckduckgo_search==4.4.3->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 14))\n",
            "  Downloading curl_cffi-0.7.1-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (13 kB)\n",
            "Collecting lxml>=5.1.0 (from duckduckgo_search==4.4.3->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 14))\n",
            "  Downloading lxml-5.2.2-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (3.4 kB)\n",
            "Requirement already satisfied: nest-asyncio>=1.6.0 in /usr/local/lib/python3.10/dist-packages (from duckduckgo_search==4.4.3->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 14)) (1.6.0)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4)) (1.3.1)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4)) (23.2.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4)) (1.4.1)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4)) (6.0.5)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4)) (1.9.4)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->openai==1.30.5->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 10)) (3.7)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->openai==1.30.5->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 10)) (1.2.2)\n",
            "Requirement already satisfied: cffi>=1.12.0 in /usr/local/lib/python3.10/dist-packages (from curl-cffi>=0.6.0b9->duckduckgo_search==4.4.3->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 14)) (1.16.0)\n",
            "Requirement already satisfied: certifi>=2024.2.2 in /usr/local/lib/python3.10/dist-packages (from curl-cffi>=0.6.0b9->duckduckgo_search==4.4.3->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 14)) (2024.7.4)\n",
            "Collecting starlette<0.38.0,>=0.37.2 (from fastapi>=0.95.2->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading starlette-0.37.2-py3-none-any.whl.metadata (5.9 kB)\n",
            "Collecting fastapi-cli>=0.0.2 (from fastapi>=0.95.2->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading fastapi_cli-0.0.4-py3-none-any.whl.metadata (7.0 kB)\n",
            "Requirement already satisfied: jinja2>=2.11.2 in /usr/local/lib/python3.10/dist-packages (from fastapi>=0.95.2->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (3.1.4)\n",
            "Collecting python-multipart>=0.0.7 (from fastapi>=0.95.2->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading python_multipart-0.0.9-py3-none-any.whl.metadata (2.5 kB)\n",
            "Collecting email_validator>=2.0.0 (from fastapi>=0.95.2->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading email_validator-2.2.0-py3-none-any.whl.metadata (25 kB)\n",
            "Collecting httpcore==1.* (from httpx<1,>=0.23.0->openai==1.30.5->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 10))\n",
            "  Downloading httpcore-1.0.5-py3-none-any.whl.metadata (20 kB)\n",
            "Collecting h11<0.15,>=0.13 (from httpcore==1.*->httpx<1,>=0.23.0->openai==1.30.5->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 10))\n",
            "  Downloading h11-0.14.0-py3-none-any.whl.metadata (8.2 kB)\n",
            "Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (1.16.0)\n",
            "Requirement already satisfied: python-dateutil>=2.5.3 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (2.8.2)\n",
            "Requirement already satisfied: google-auth>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (2.27.0)\n",
            "Requirement already satisfied: websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (1.8.0)\n",
            "Requirement already satisfied: requests-oauthlib in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (1.3.1)\n",
            "Requirement already satisfied: oauthlib>=3.2.2 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (3.2.2)\n",
            "Requirement already satisfied: urllib3>=1.24.2 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (2.0.7)\n",
            "Collecting dataclasses-json<0.7,>=0.5.7 (from langchain-community<0.3.0,>=0.2.6->langchain-experimental==0.0.62->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 5))\n",
            "  Downloading dataclasses_json-0.6.7-py3-none-any.whl.metadata (25 kB)\n",
            "Collecting jsonpatch<2.0,>=1.33 (from langchain-core<0.3.0,>=0.2.20->langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4))\n",
            "  Downloading jsonpatch-1.33-py2.py3-none-any.whl.metadata (3.0 kB)\n",
            "Requirement already satisfied: packaging<25,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.3.0,>=0.2.20->langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4)) (24.1)\n",
            "Collecting orjson<4.0.0,>=3.9.14 (from langsmith<0.2.0,>=0.1.17->langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4))\n",
            "  Downloading orjson-3.10.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (50 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m50.4/50.4 kB\u001b[0m \u001b[31m2.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting coloredlogs (from onnxruntime>=1.14.1->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading coloredlogs-15.0.1-py2.py3-none-any.whl.metadata (12 kB)\n",
            "Requirement already satisfied: flatbuffers in /usr/local/lib/python3.10/dist-packages (from onnxruntime>=1.14.1->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (24.3.25)\n",
            "Requirement already satisfied: protobuf in /usr/local/lib/python3.10/dist-packages (from onnxruntime>=1.14.1->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (3.20.3)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from onnxruntime>=1.14.1->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (1.13.1)\n",
            "Collecting deprecated>=1.2.6 (from opentelemetry-api>=1.2.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading Deprecated-1.2.14-py2.py3-none-any.whl.metadata (5.4 kB)\n",
            "Collecting importlib-metadata<=8.0.0,>=6.0 (from opentelemetry-api>=1.2.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading importlib_metadata-8.0.0-py3-none-any.whl.metadata (4.6 kB)\n",
            "Requirement already satisfied: googleapis-common-protos~=1.52 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (1.63.2)\n",
            "Collecting opentelemetry-exporter-otlp-proto-common==1.26.0 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading opentelemetry_exporter_otlp_proto_common-1.26.0-py3-none-any.whl.metadata (1.8 kB)\n",
            "Collecting opentelemetry-proto==1.26.0 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading opentelemetry_proto-1.26.0-py3-none-any.whl.metadata (2.3 kB)\n",
            "Collecting opentelemetry-semantic-conventions==0.47b0 (from opentelemetry-sdk>=1.2.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading opentelemetry_semantic_conventions-0.47b0-py3-none-any.whl.metadata (2.4 kB)\n",
            "Collecting monotonic>=1.5 (from posthog>=2.4.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading monotonic-1.6-py2.py3-none-any.whl.metadata (1.5 kB)\n",
            "Collecting backoff>=1.10.0 (from posthog>=2.4.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading backoff-2.2.1-py3-none-any.whl.metadata (14 kB)\n",
            "Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic>=1.9->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.20.1 in /usr/local/lib/python3.10/dist-packages (from pydantic>=1.9->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (2.20.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.28->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (3.3.2)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4)) (3.0.3)\n",
            "Requirement already satisfied: regex>=2022.1.18 in /usr/local/lib/python3.10/dist-packages (from tiktoken<1,>=0.7->langchain-openai==0.1.7->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 7)) (2024.5.15)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.16.4 in /usr/local/lib/python3.10/dist-packages (from tokenizers>=0.13.2->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (0.23.5)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from typer>=0.9.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (1.5.4)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from typer>=0.9.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (13.7.1)\n",
            "Collecting httptools>=0.5.0 (from uvicorn[standard]>=0.18.3->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading httptools-0.6.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.6 kB)\n",
            "Collecting python-dotenv>=0.13 (from uvicorn[standard]>=0.18.3->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)\n",
            "Collecting uvloop!=0.15.0,!=0.15.1,>=0.14.0 (from uvicorn[standard]>=0.18.3->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading uvloop-0.19.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)\n",
            "Collecting watchfiles>=0.13 (from uvicorn[standard]>=0.18.3->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading watchfiles-0.22.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)\n",
            "Collecting websockets>=10.4 (from uvicorn[standard]>=0.18.3->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading websockets-12.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi>=1.12.0->curl-cffi>=0.6.0b9->duckduckgo_search==4.4.3->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 14)) (2.22)\n",
            "Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json<0.7,>=0.5.7->langchain-community<0.3.0,>=0.2.6->langchain-experimental==0.0.62->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 5))\n",
            "  Downloading marshmallow-3.21.3-py3-none-any.whl.metadata (7.1 kB)\n",
            "Collecting typing-inspect<1,>=0.4.0 (from dataclasses-json<0.7,>=0.5.7->langchain-community<0.3.0,>=0.2.6->langchain-experimental==0.0.62->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 5))\n",
            "  Downloading typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)\n",
            "Requirement already satisfied: wrapt<2,>=1.10 in /usr/local/lib/python3.10/dist-packages (from deprecated>=1.2.6->opentelemetry-api>=1.2.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (1.14.1)\n",
            "Collecting dnspython>=2.0.0 (from email_validator>=2.0.0->fastapi>=0.95.2->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading dnspython-2.6.1-py3-none-any.whl.metadata (5.8 kB)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (5.4.0)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (0.4.0)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (4.9)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers>=0.13.2->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (3.15.4)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers>=0.13.2->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (2024.6.1)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata<=8.0.0,>=6.0->opentelemetry-api>=1.2.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (3.19.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2>=2.11.2->fastapi>=0.95.2->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (2.1.5)\n",
            "Collecting jsonpointer>=1.9 (from jsonpatch<2.0,>=1.33->langchain-core<0.3.0,>=0.2.20->langchain==0.2.9->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 4))\n",
            "  Downloading jsonpointer-3.0.0-py2.py3-none-any.whl.metadata (2.3 kB)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->typer>=0.9.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->typer>=0.9.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (2.16.1)\n",
            "Collecting humanfriendly>=9.1 (from coloredlogs->onnxruntime>=1.14.1->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2))\n",
            "  Downloading humanfriendly-10.0-py2.py3-none-any.whl.metadata (9.2 kB)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from sympy->onnxruntime>=1.14.1->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (1.3.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer>=0.9.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (0.1.2)\n",
            "Requirement already satisfied: pyasn1<0.7.0,>=0.4.6 in /usr/local/lib/python3.10/dist-packages (from pyasn1-modules>=0.2.1->google-auth>=1.0.1->kubernetes>=28.1.0->chromadb==0.4.15->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 2)) (0.6.0)\n",
            "Collecting mypy-extensions>=0.3.0 (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain-community<0.3.0,>=0.2.6->langchain-experimental==0.0.62->-r /content/AgenticAI_GenAIHack/requirements_agenti_ai.txt (line 5))\n",
            "  Downloading mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)\n",
            "Downloading beautifulsoup4-4.12.2-py3-none-any.whl (142 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m143.0/143.0 kB\u001b[0m \u001b[31m6.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading chromadb-0.4.15-py3-none-any.whl (479 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m479.8/479.8 kB\u001b[0m \u001b[31m15.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain-0.2.9-py3-none-any.whl (987 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m987.7/987.7 kB\u001b[0m \u001b[31m22.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain_experimental-0.0.62-py3-none-any.whl (202 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m202.7/202.7 kB\u001b[0m \u001b[31m14.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain_postgres-0.0.6-py3-none-any.whl (18 kB)\n",
            "Downloading langchain_openai-0.1.7-py3-none-any.whl (34 kB)\n",
            "Downloading langgraph-0.0.55-py3-none-any.whl (84 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m84.1/84.1 kB\u001b[0m \u001b[31m5.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading Markdown-3.5.2-py3-none-any.whl (103 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m103.9/103.9 kB\u001b[0m \u001b[31m6.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading openai-1.30.5-py3-none-any.whl (320 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m320.7/320.7 kB\u001b[0m \u001b[31m16.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain_chroma-0.1.2-py3-none-any.whl (9.3 kB)\n",
            "Downloading tavily_python-0.3.5-py3-none-any.whl (13 kB)\n",
            "Downloading simple_colors-0.1.5-py3-none-any.whl (2.8 kB)\n",
            "Downloading duckduckgo_search-4.4.3-py3-none-any.whl (20 kB)\n",
            "Downloading chroma_hnswlib-0.7.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.4/2.4 MB\u001b[0m \u001b[31m56.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading bcrypt-4.2.0-cp39-abi3-manylinux_2_28_x86_64.whl (273 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m273.8/273.8 kB\u001b[0m \u001b[31m17.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading curl_cffi-0.7.1-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (6.1 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.1/6.1 MB\u001b[0m \u001b[31m67.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading fastapi-0.111.1-py3-none-any.whl (92 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m92.2/92.2 kB\u001b[0m \u001b[31m5.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading httpx-0.27.0-py3-none-any.whl (75 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m75.6/75.6 kB\u001b[0m \u001b[31m3.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading httpcore-1.0.5-py3-none-any.whl (77 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m77.9/77.9 kB\u001b[0m \u001b[31m4.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading kubernetes-30.1.0-py2.py3-none-any.whl (1.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.7/1.7 MB\u001b[0m \u001b[31m54.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain_community-0.2.10-py3-none-any.whl (2.3 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.3/2.3 MB\u001b[0m \u001b[31m59.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain_core-0.2.24-py3-none-any.whl (377 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m377.3/377.3 kB\u001b[0m \u001b[31m23.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain_text_splitters-0.2.2-py3-none-any.whl (25 kB)\n",
            "Downloading langsmith-0.1.93-py3-none-any.whl (139 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m139.8/139.8 kB\u001b[0m \u001b[31m10.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading lxml-5.2.2-cp310-cp310-manylinux_2_28_x86_64.whl (5.0 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m5.0/5.0 MB\u001b[0m \u001b[31m67.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading onnxruntime-1.18.1-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (6.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.8/6.8 MB\u001b[0m \u001b[31m69.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading opentelemetry_api-1.26.0-py3-none-any.whl (61 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m61.5/61.5 kB\u001b[0m \u001b[31m4.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading opentelemetry_exporter_otlp_proto_grpc-1.26.0-py3-none-any.whl (18 kB)\n",
            "Downloading opentelemetry_exporter_otlp_proto_common-1.26.0-py3-none-any.whl (17 kB)\n",
            "Downloading opentelemetry_proto-1.26.0-py3-none-any.whl (52 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m52.5/52.5 kB\u001b[0m \u001b[31m3.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading opentelemetry_sdk-1.26.0-py3-none-any.whl (109 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m109.5/109.5 kB\u001b[0m \u001b[31m7.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading opentelemetry_semantic_conventions-0.47b0-py3-none-any.whl (138 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m138.0/138.0 kB\u001b[0m \u001b[31m9.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading overrides-7.7.0-py3-none-any.whl (17 kB)\n",
            "Downloading pgvector-0.2.5-py2.py3-none-any.whl (9.6 kB)\n",
            "Downloading posthog-3.5.0-py2.py3-none-any.whl (41 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m41.3/41.3 kB\u001b[0m \u001b[31m2.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading psycopg-3.2.1-py3-none-any.whl (197 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m197.7/197.7 kB\u001b[0m \u001b[31m15.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading psycopg_pool-3.2.2-py3-none-any.whl (38 kB)\n",
            "Downloading pulsar_client-3.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m5.4/5.4 MB\u001b[0m \u001b[31m67.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading tiktoken-0.7.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.1 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.1/1.1 MB\u001b[0m \u001b[31m41.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading uuid6-2024.7.10-py3-none-any.whl (6.4 kB)\n",
            "Downloading uvicorn-0.30.3-py3-none-any.whl (62 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.8/62.8 kB\u001b[0m \u001b[31m4.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading backoff-2.2.1-py3-none-any.whl (15 kB)\n",
            "Downloading dataclasses_json-0.6.7-py3-none-any.whl (28 kB)\n",
            "Downloading Deprecated-1.2.14-py2.py3-none-any.whl (9.6 kB)\n",
            "Downloading email_validator-2.2.0-py3-none-any.whl (33 kB)\n",
            "Downloading fastapi_cli-0.0.4-py3-none-any.whl (9.5 kB)\n",
            "Downloading h11-0.14.0-py3-none-any.whl (58 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m58.3/58.3 kB\u001b[0m \u001b[31m4.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading httptools-0.6.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (341 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m341.4/341.4 kB\u001b[0m \u001b[31m22.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading importlib_metadata-8.0.0-py3-none-any.whl (24 kB)\n",
            "Downloading jsonpatch-1.33-py2.py3-none-any.whl (12 kB)\n",
            "Downloading monotonic-1.6-py2.py3-none-any.whl (8.2 kB)\n",
            "Downloading orjson-3.10.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (141 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m141.1/141.1 kB\u001b[0m \u001b[31m8.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)\n",
            "Downloading python_multipart-0.0.9-py3-none-any.whl (22 kB)\n",
            "Downloading starlette-0.37.2-py3-none-any.whl (71 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m71.9/71.9 kB\u001b[0m \u001b[31m4.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading uvloop-0.19.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.4/3.4 MB\u001b[0m \u001b[31m46.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchfiles-0.22.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.2 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.2/1.2 MB\u001b[0m \u001b[31m40.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading websockets-12.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (130 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m130.2/130.2 kB\u001b[0m \u001b[31m8.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m46.0/46.0 kB\u001b[0m \u001b[31m2.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading dnspython-2.6.1-py3-none-any.whl (307 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m307.7/307.7 kB\u001b[0m \u001b[31m20.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading humanfriendly-10.0-py2.py3-none-any.whl (86 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m86.8/86.8 kB\u001b[0m \u001b[31m5.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading jsonpointer-3.0.0-py2.py3-none-any.whl (7.6 kB)\n",
            "Downloading marshmallow-3.21.3-py3-none-any.whl (49 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m49.2/49.2 kB\u001b[0m \u001b[31m3.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)\n",
            "Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)\n",
            "Building wheels for collected packages: google-search-results, pypika\n",
            "  Building wheel for google-search-results (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for google-search-results: filename=google_search_results-2.4.2-py3-none-any.whl size=32010 sha256=e8cd1ebe6c6f39571f82b9347a0652c6a81ea15be0f92dcb5947fa3334f32eca\n",
            "  Stored in directory: /root/.cache/pip/wheels/d3/b2/c3/03302d12bb44a2cdff3c9371f31b72c0c4e84b8d2285eeac53\n",
            "  Building wheel for pypika (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pypika: filename=PyPika-0.48.9-py2.py3-none-any.whl size=53725 sha256=2b98d986cafcde1dd8ba7c46854e7495d77debc8618a1d4817f5e64e607c60f1\n",
            "  Stored in directory: /root/.cache/pip/wheels/e1/26/51/d0bffb3d2fd82256676d7ad3003faea3bd6dddc9577af665f4\n",
            "Successfully built google-search-results pypika\n",
            "Installing collected packages: simple-colors, pypika, monotonic, websockets, uvloop, uuid6, python-multipart, python-dotenv, pulsar-client, psycopg-pool, psycopg, pgvector, overrides, orjson, opentelemetry-proto, mypy-extensions, marshmallow, Markdown, lxml, jsonpointer, importlib-metadata, humanfriendly, httptools, h11, dnspython, deprecated, chroma-hnswlib, beautifulsoup4, bcrypt, backoff, watchfiles, uvicorn, typing-inspect, tiktoken, starlette, posthog, opentelemetry-exporter-otlp-proto-common, opentelemetry-api, jsonpatch, httpcore, google-search-results, email_validator, curl-cffi, coloredlogs, opentelemetry-semantic-conventions, onnxruntime, langsmith, kubernetes, httpx, duckduckgo_search, dataclasses-json, tavily-python, opentelemetry-sdk, openai, langchain-core, fastapi-cli, opentelemetry-exporter-otlp-proto-grpc, langgraph, langchain-text-splitters, langchain-postgres, langchain-openai, fastapi, langchain, chromadb, langchain-community, langchain-chroma, langchain-experimental\n",
            "  Attempting uninstall: Markdown\n",
            "    Found existing installation: Markdown 3.6\n",
            "    Uninstalling Markdown-3.6:\n",
            "      Successfully uninstalled Markdown-3.6\n",
            "  Attempting uninstall: lxml\n",
            "    Found existing installation: lxml 4.9.4\n",
            "    Uninstalling lxml-4.9.4:\n",
            "      Successfully uninstalled lxml-4.9.4\n",
            "  Attempting uninstall: importlib-metadata\n",
            "    Found existing installation: importlib_metadata 8.2.0\n",
            "    Uninstalling importlib_metadata-8.2.0:\n",
            "      Successfully uninstalled importlib_metadata-8.2.0\n",
            "  Attempting uninstall: beautifulsoup4\n",
            "    Found existing installation: beautifulsoup4 4.12.3\n",
            "    Uninstalling beautifulsoup4-4.12.3:\n",
            "      Successfully uninstalled beautifulsoup4-4.12.3\n",
            "Successfully installed Markdown-3.5.2 backoff-2.2.1 bcrypt-4.2.0 beautifulsoup4-4.12.2 chroma-hnswlib-0.7.3 chromadb-0.4.15 coloredlogs-15.0.1 curl-cffi-0.7.1 dataclasses-json-0.6.7 deprecated-1.2.14 dnspython-2.6.1 duckduckgo_search-4.4.3 email_validator-2.2.0 fastapi-0.111.1 fastapi-cli-0.0.4 google-search-results-2.4.2 h11-0.14.0 httpcore-1.0.5 httptools-0.6.1 httpx-0.27.0 humanfriendly-10.0 importlib-metadata-8.0.0 jsonpatch-1.33 jsonpointer-3.0.0 kubernetes-30.1.0 langchain-0.2.9 langchain-chroma-0.1.2 langchain-community-0.2.10 langchain-core-0.2.24 langchain-experimental-0.0.62 langchain-openai-0.1.7 langchain-postgres-0.0.6 langchain-text-splitters-0.2.2 langgraph-0.0.55 langsmith-0.1.93 lxml-5.2.2 marshmallow-3.21.3 monotonic-1.6 mypy-extensions-1.0.0 onnxruntime-1.18.1 openai-1.30.5 opentelemetry-api-1.26.0 opentelemetry-exporter-otlp-proto-common-1.26.0 opentelemetry-exporter-otlp-proto-grpc-1.26.0 opentelemetry-proto-1.26.0 opentelemetry-sdk-1.26.0 opentelemetry-semantic-conventions-0.47b0 orjson-3.10.6 overrides-7.7.0 pgvector-0.2.5 posthog-3.5.0 psycopg-3.2.1 psycopg-pool-3.2.2 pulsar-client-3.5.0 pypika-0.48.9 python-dotenv-1.0.1 python-multipart-0.0.9 simple-colors-0.1.5 starlette-0.37.2 tavily-python-0.3.5 tiktoken-0.7.0 typing-inspect-0.9.0 uuid6-2024.7.10 uvicorn-0.30.3 uvloop-0.19.0 watchfiles-0.22.0 websockets-12.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "os.chdir(\"/content/AgenticAI_GenAIHack\")"
      ],
      "metadata": {
        "id": "fOPlwCtRiyW5"
      },
      "id": "fOPlwCtRiyW5",
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "id": "9dee900e-7a1c-48f2-b2b9-c45296e1f67e",
      "metadata": {
        "tags": [],
        "id": "9dee900e-7a1c-48f2-b2b9-c45296e1f67e",
        "outputId": "d2ac13b8-1b64-4dee-e6ad-9e24ed245cb3",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:langchain_community.utils.user_agent:USER_AGENT environment variable not set, consider setting it to identify your requests.\n"
          ]
        }
      ],
      "source": [
        "import warnings\n",
        "warnings.filterwarnings(\"ignore\")\n",
        "from typing import Literal\n",
        "from typing import List, Sequence\n",
        "import random\n",
        "import numpy as np\n",
        "from bs4 import BeautifulSoup\n",
        "import functools, operator, requests, os, json\n",
        "from langchain.agents import AgentExecutor, create_openai_tools_agent\n",
        "from langchain_core.messages import BaseMessage, HumanMessage\n",
        "\n",
        "from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser\n",
        "from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate\n",
        "from langgraph.graph import StateGraph, END\n",
        "from langchain.tools import tool\n",
        "from typing import Annotated, Any, Dict, List, Optional, Sequence, TypedDict\n",
        "from IPython.display import Markdown, JSON\n",
        "\n",
        "from langchain.text_splitter import RecursiveCharacterTextSplitter\n",
        "from langchain_community.document_loaders import WebBaseLoader\n",
        "from langchain_community.vectorstores import Chroma\n",
        "from langchain_openai import OpenAIEmbeddings\n",
        "from langchain.tools.retriever import create_retriever_tool\n",
        "from langchain_community.utilities import BingSearchAPIWrapper\n",
        "from langchain.agents import Tool\n",
        "from langgraph.checkpoint.sqlite import SqliteSaver\n",
        "from langchain_community.callbacks import get_openai_callback\n",
        "\n",
        "from langchain_core.output_parsers import PydanticOutputParser\n",
        "from langchain_core.pydantic_v1 import BaseModel, Field, validator\n",
        "from langchain_core.output_parsers import JsonOutputParser\n",
        "import ast\n",
        "import re\n",
        "\n",
        "from prompts import *\n",
        "from utils import create_MVR, create_qa_agent, create_chat_agent"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "7b0657c0-3356-40c1-a036-37989dc82268",
      "metadata": {
        "id": "7b0657c0-3356-40c1-a036-37989dc82268"
      },
      "source": [
        "#### Load environment variables"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "id": "a86c9ff2-5905-49bb-ae97-d1f08d55af96",
      "metadata": {
        "tags": [],
        "id": "a86c9ff2-5905-49bb-ae97-d1f08d55af96"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "from dotenv import load_dotenv\n",
        "load_dotenv(dotenv_path=\"/content/AgenticAI_GenAIHack/env\")\n",
        "\n",
        "EMBEDDING_DEPLOYMENT_NAME = os.getenv('EMBEDDING_3_DEPLOYMENT_NAME')\n",
        "EMBEDDING_API_KEY = os.getenv('EMBEDDING_3_API_KEY')\n",
        "EMBEDDING_API_BASE = os.getenv('EMBEDDING_3_API_BASE')\n",
        "\n",
        "GPT4_TURBO_DEPLOYMENT_NAME = os.getenv('GPT4_TURBO_DEPLOYMENT_NAME')\n",
        "GPT4_OMNI_DEPLOYMENT_NAME = os.getenv('GPT4o_DEPLOYMENT_NAME')\n",
        "\n",
        "API_KEY = os.getenv('sweden_API_KEY')\n",
        "API_BASE = os.getenv('sweden_API_BASE')\n",
        "API_TYPE = os.getenv('API_TYPE')\n",
        "API_VERSION = os.getenv('API_VERSION')"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "9a70f67a-75f1-4510-a7c3-293d60c63e23",
      "metadata": {
        "id": "9a70f67a-75f1-4510-a7c3-293d60c63e23"
      },
      "source": [
        "#### Define LLM"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "id": "501ecc9a-5333-45d6-8f0a-99f5006b485e",
      "metadata": {
        "tags": [],
        "id": "501ecc9a-5333-45d6-8f0a-99f5006b485e"
      },
      "outputs": [],
      "source": [
        "from langchain_openai import AzureChatOpenAI\n",
        "from langchain_openai import AzureOpenAIEmbeddings\n",
        "\n",
        "embeddings = AzureOpenAIEmbeddings(\n",
        "    azure_deployment=EMBEDDING_DEPLOYMENT_NAME,\n",
        "    openai_api_key=EMBEDDING_API_KEY,\n",
        "    azure_endpoint=EMBEDDING_API_BASE,\n",
        "    openai_api_version=API_VERSION,\n",
        ")\n",
        "\n",
        "llm = AzureChatOpenAI(\n",
        "        azure_endpoint=API_BASE,\n",
        "        openai_api_version=API_VERSION,\n",
        "        azure_deployment=GPT4_OMNI_DEPLOYMENT_NAME,\n",
        "        openai_api_key=API_KEY,\n",
        "        openai_api_type=API_TYPE,\n",
        "        temperature=0)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "c6e31069-d8df-43f6-95d8-3b3ea79e872a",
      "metadata": {
        "id": "c6e31069-d8df-43f6-95d8-3b3ea79e872a"
      },
      "source": [
        "### Define Tools"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "CLiuj-GMGvo0",
        "outputId": "81867d81-aeca-4f05-ac55-c287c433b5cf",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "id": "CLiuj-GMGvo0",
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "id": "188a96af-fcba-440c-9383-c800ef0f739d",
      "metadata": {
        "tags": [],
        "id": "188a96af-fcba-440c-9383-c800ef0f739d"
      },
      "outputs": [],
      "source": [
        "## Retriever Creation\n",
        "\n",
        "vector_store_exists = True\n",
        "\n",
        "_IFRS_ret = create_MVR('IFRS.pickle', embeddings, \"IFRS\", vectorstore_exists=vector_store_exists, k=7)\n",
        "\n",
        "_annual_reports_ret = create_MVR('kpmg.pickle', embeddings, \"ANNUAL_REPORTS\", vectorstore_exists=vector_store_exists, k=7)\n",
        "\n",
        "_audit_ret = create_MVR('kpmg.pickle', embeddings, \"KPMG\", vectorstore_exists=vector_store_exists, k=7)\n",
        "\n",
        "## Tool Creation\n",
        "\n",
        "IFRS_tool = create_retriever_tool(retriever=_IFRS_ret,\n",
        "                                  name = 'IFRS_Retriever',\n",
        "                                  description=\"Use this tool to answer questions related to IFRS which is International Financial Reporting Standards.\")\n",
        "\n",
        "ANNUAL_REPORTS_tool = create_retriever_tool(retriever = _annual_reports_ret,\n",
        "                                        name = \"ANNUAL_REPORTS_RETRIEVER\",\n",
        "                                        description = \"Use this tool when you need to answer questions related to annual reports, 10K reports or 20F reports of Novartis and it's competitors ('Roche','GSK','Bayer','AstraZeneca','Sanofi', 'Amgen','Abbvie', 'BMS' - Bristol Myers Squibb, 'Gilead', 'Eli Lilly', 'Merck', 'Pfizer', 'Takeda','Johnson&Johnson', 'novo-nordisk'). If no specific year is mentioned in the question, always look for latest available year\")\n",
        "\n",
        "AUDIT_tool = create_retriever_tool(retriever=_audit_ret,\n",
        "                              name = 'AUDIT_Retriever',\n",
        "                              description=\"Use this tool to answer questions related to the Auditor(KPMG, EY, PWC) Insights on IFRS which is International Financial Reporting Standards\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "id": "9ca49edf-26a4-4019-80c1-4fe9b18152f8",
      "metadata": {
        "tags": [],
        "id": "9ca49edf-26a4-4019-80c1-4fe9b18152f8"
      },
      "outputs": [],
      "source": [
        "class CheckNodeState(TypedDict):\n",
        "    \"\"\"\n",
        "    Represents the state of check nodes.\n",
        "\n",
        "    Attributes:\n",
        "        observation: observation found from the check node\n",
        "    \"\"\"\n",
        "    observation: str\n",
        "\n",
        "\n",
        "class SourceDetectNodeState(TypedDict):\n",
        "    \"\"\"\n",
        "    Represents the state of check nodes.\n",
        "\n",
        "    Attributes:\n",
        "        observation: observation found from the check node\n",
        "    \"\"\"\n",
        "    observation: List[str]\n",
        "\n",
        "\n",
        "\n",
        "class ResponseNodeState(TypedDict):\n",
        "    \"\"\"\n",
        "    Represents the state of Response nodes.\n",
        "\n",
        "    Attributes:\n",
        "        answer: answer generated\n",
        "        metadata: metadata of the answer generated\n",
        "    \"\"\"\n",
        "\n",
        "    answer: str\n",
        "    metadata: Annotated[dict, operator.add]\n",
        "\n",
        "\n",
        "\n",
        "def topic_modelling_node(state):\n",
        "    \"\"\"Use this tool to run topic modelling module and update the database with Question and Topic\"\"\"\n",
        "    print(\"------ENTERING: TOPIC MODELLING NODE------\")\n",
        "    ## Write code here to get web answer\n",
        "\n",
        "    print(\"============================================\")\n",
        "    print(state)\n",
        "    print(\"============================================\")\n",
        "\n",
        "    topic = \"DUMMY TOPIC\"\n",
        "    print(f\"------OBSERVATION: {topic}------\")\n",
        "    return {\"topic\": topic}\n",
        "\n",
        "\n",
        "class FinanceCheck_class(BaseModel):\n",
        "    \"\"\"Binary score for finance check on the user question.\"\"\"\n",
        "    binary_score: str = Field(description=\"Given a user question, return 'Yes' if is related to Finance/Accounting/Reporting else 'No'\")\n",
        "\n",
        "\n",
        "def get_finance_check(_llm, META_RESPONSE_PROMPT, state):\n",
        "    parser = PydanticOutputParser(pydantic_object=FinanceCheck_class)\n",
        "    prompt = PromptTemplate(template=META_RESPONSE_PROMPT,\n",
        "                            input_variables=[\"question\"],\n",
        "                            partial_variables={\"format_instructions\": parser.get_format_instructions()},\n",
        "                           )\n",
        "    prompt_and_model = prompt | llm\n",
        "\n",
        "    with get_openai_callback() as cb:\n",
        "        output = prompt_and_model.invoke({\"question\": question})\n",
        "        result = parser.invoke(output)\n",
        "    return result.binary_score\n",
        "\n",
        "\n",
        "def finance_check_node(state):\n",
        "    \"\"\"Use this tool to check whether the user question is about finance or general greeting.\"\"\"\n",
        "    observation = get_finance_check(llm, META_RESPONSE_PROMPT_DETAILED, state['question']) # random.choice([\"Yes\", \"No\"])\n",
        "\n",
        "    print(\"------ENTERING: FINANCE CHECK NODE------\")\n",
        "    print(f\"------OBSERVATION: {observation}------\")\n",
        "\n",
        "    finance_check: CheckNodeState = {\"observation\": observation}\n",
        "\n",
        "    return {\"finance_check\": finance_check}\n",
        "\n",
        "\n",
        "def get_generic_answer(_llm, META_ANSWER_PROMPT, question):\n",
        "    with get_openai_callback() as cb:\n",
        "        response = _llm.invoke(META_ANSWER_PROMPT.format(question=question))\n",
        "    return response.content\n",
        "\n",
        "\n",
        "def generic_response_node(state):\n",
        "    \"\"\"Use this tool to answer user generic questions\"\"\"\n",
        "    print(\"------ENTERING: GENERIC RESPONSE NODE------\")\n",
        "\n",
        "    answer = get_generic_answer(llm, META_ANSWER_PROMPT, state['question'])\n",
        "\n",
        "    generic_response: ResponseNodeState = {\"answer\": answer,\n",
        "                                            \"metadata\": []}\n",
        "\n",
        "    print(f\"------ANSWER: {generic_response}------\")\n",
        "    return {\"generic_response\": generic_responsec, \"final_answer\": answer}\n",
        "\n",
        "\n",
        "class RouteQuery_class(BaseModel):\n",
        "    \"\"\"Route a user query to the most relevant datasource.\"\"\"\n",
        "    datasource: Literal[\"FRA\", \"WEB\"] = Field(description=\"Given a user question choose to route it to WEB or FRA.\")\n",
        "\n",
        "def get_query_rerouter_check(llm, QUERY_REROUTER_PROMPT, state):\n",
        "    parser = PydanticOutputParser(pydantic_object=RouteQuery_class)\n",
        "\n",
        "    prompt = PromptTemplate(template=QUERY_REROUTER_PROMPT,\n",
        "                            input_variables=[\"question\"],\n",
        "                            partial_variables={\"format_instructions\": parser.get_format_instructions()},\n",
        "                           )\n",
        "    prompt_and_model = prompt | llm\n",
        "\n",
        "    with get_openai_callback() as cb:\n",
        "        output = prompt_and_model.invoke({\"question\": question})\n",
        "        query_rerouter_check = parser.invoke(output)\n",
        "\n",
        "    return query_rerouter_check.datasource\n",
        "\n",
        "\n",
        "def query_rerouter_node(state):\n",
        "    \"\"\"Use this tool to check whether the user question needs an internet search to answer\"\"\"\n",
        "    print(\"------ENTERING: QUERY REROUTER NODE------\")\n",
        "    observation = get_query_rerouter_check(llm, QUERY_REROUTER_PROMPT_DETAILED, state['question']) # random.choice([\"Yes\", \"No\"])\n",
        "\n",
        "    print(f\"------OBSERVATION: {observation}------\")\n",
        "    query_rerouter_check: CheckNodeState = {\"observation\": observation}\n",
        "    return {\"query_rerouter_check\": query_rerouter_check}\n",
        "\n",
        "\n",
        "\n",
        "def human_check_node(state):\n",
        "    user_input = input(\"The answer is not available from the private data sources! Do you want me to search over the internet to answer?\")\n",
        "    human_response: ResponseNodeState = {\"answer\": user_input.lower(),\n",
        "                                            \"metadata\": []}\n",
        "    return {\"human_response\": human_response}\n",
        "\n",
        "\n",
        "\n",
        "# Create a tool to processes content from a webpage\n",
        "@tool(\"process_content\", return_direct=False)\n",
        "def process_content(url: str, chunk_size: int = 10000) -> str:\n",
        "    \"\"\"\n",
        "    Use this tool to extract content from HTML pages and chunk it recursively.\n",
        "\n",
        "    Args:\n",
        "      url (str): The URL of the HTML page to process.\n",
        "      chunk_size (int, optional): The maximum size of each text chunk. Defaults to 100000.\n",
        "\n",
        "    Returns:\n",
        "      str: The chunked text content extracted from the HTML page.\n",
        "    \"\"\"\n",
        "    response = requests.get(url)\n",
        "    soup = BeautifulSoup(response.content, 'html.parser',from_encoding=\"iso-8859-1\")\n",
        "    text = soup.get_text()\n",
        "\n",
        "    def chunk_text(text, chunk_size):\n",
        "        if len(text) <= chunk_size:\n",
        "            return text\n",
        "        else:\n",
        "            midpoint = len(text) // 2\n",
        "            left_chunk = chunk_text(text[:midpoint], chunk_size)\n",
        "            right_chunk = chunk_text(text[midpoint:], chunk_size)\n",
        "            return left_chunk + \"\\n\" + right_chunk\n",
        "\n",
        "        chunks = chunk_text(text, chunk_size)\n",
        "        return chunks\n",
        "\n",
        "\n",
        "@tool(\"bing_search\", return_direct=False)\n",
        "def bing_search(query: str) -> str:\n",
        "    \"\"\"Use this tool when you need to answer questions related to current events and latest happenings\"\"\"\n",
        "    bing_search = BingSearchAPIWrapper()\n",
        "    results = bing_search.results(query, 5)\n",
        "    return results if results else \"No results found.\"\n",
        "\n",
        "\n",
        "def get_web_search_answer(state):\n",
        "    tools = [bing_search, process_content]\n",
        "\n",
        "    generate_prompt = \"\"\"You are a web searcher trained to retrieve the current events from the internet. Search the internet for information.\n",
        "                            Generate the best answer possible for the user's request with mandatory mention of the sources and the hyperlinks for the sources wherever it is possible.\n",
        "                            Think step by step. Breakdown the question if it has multiple asks and finally merge your results.\n",
        "                            Always crave for the best version of answer.\n",
        "                            - **Always** before giving the final answer, try another method.Then reflect on the answers of the two methods you did and ask yourself if it answers correctly the original question. If you are not sure, try another method.\n",
        "                            - If the methods tried do not give the same result, reflect and try again until you have two methods that have the same result.\n",
        "                            - If you are sure of the correct answer, create a beautiful and thorough response.\n",
        "                            ** DO NOT MAKE UP AN ANSWER OR USE YOUR PRIOR KNOWLEDGE, ONLY USE THE RESULTS OF THE CALCULATIONS YOU HAVE DONE **\n",
        "                            PLEASE NOTE THAT IF NO SPECIFIC YEAR MENTIONED IN THE QUESTION, ALWAYS LOOK FOR THE LATEST YEAR.\n",
        "                            \"\"\"\n",
        "\n",
        "    generate_agent = create_qa_agent(llm, tools, generate_prompt, verbose=False)\n",
        "    with get_openai_callback() as cb:\n",
        "        answer = generate_agent.invoke({\"input\": state['question']})\n",
        "    return answer['output']\n",
        "\n",
        "def web_search_node(state):\n",
        "    \"\"\"Use this tool when you need to answer questions related to current events and latest happenings\"\"\"\n",
        "    print(\"------ENTERING: WEB SEARCH NODE------\")\n",
        "    ## Write code here to get answer\n",
        "    response = get_web_search_answer(state)\n",
        "    print(f\"------WEB SEARCH ANSWER: {response}------\")\n",
        "    web_response: ResponseNodeState = {\"answer\": response,\n",
        "                                        \"metadata\": []}\n",
        "    return {\"web_response\": web_response, \"final_answer\": response}\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "def get_source_detector_check(llm, SOURCE_DETECTOR_PROMPT, selected_source_list, question):\n",
        "    parser = JsonOutputParser()\n",
        "    prompt = PromptTemplate(template=SOURCE_DETECTOR_PROMPT,\n",
        "                            input_variables=[\"question\"],\n",
        "                            partial_variables={\"role_based_sources\": selected_source_list , \"format_instructions\": parser.get_format_instructions()},\n",
        "                           )\n",
        "    chain = prompt | llm | parser\n",
        "    source_detector_check = chain.invoke({\"question\": question})\n",
        "\n",
        "    return source_detector_check['Output']\n",
        "\n",
        "\n",
        "def source_detector_node(state):\n",
        "    \"\"\"Use this tool to detect the sources needed for the question to answer\"\"\"\n",
        "    print(\"------ENTERING: SOURCE DETECTOR NODE------\")\n",
        "\n",
        "    selected_source_list = [\"ifrs_answer_node\", \"annual_reports_answer_node\", \"auditor_guidance_answer_node\"]\n",
        "    sources_detected = get_source_detector_check(llm, SOURCE_DETECTOR_PROMPT_DETAILED, selected_source_list, state['question'])\n",
        "    print(sources_detected)\n",
        "    print(f\"------SOURCES DETECTED: {list(set(sources_detected))}------\")\n",
        "    source_detector_check: SourceDetectNodeState = {\"observation\": list(set(sources_detected))}\n",
        "    return {\"source_detector_check\": source_detector_check}\n",
        "\n",
        "\n",
        "def ifrs_answer_node(state):\n",
        "    \"\"\"Use this tool to answer ifrs related questions\"\"\"\n",
        "    print(\"------ENTERING: IFRS ANSWER NODE------\")\n",
        "\n",
        "    tools = [IFRS_tool]\n",
        "    generate_agent = create_qa_agent(llm, tools, IFRS_di_prompt, verbose=False)\n",
        "    with get_openai_callback() as cb:\n",
        "        answer = generate_agent.invoke({\"input\":state['question']})\n",
        "    display(Markdown(f\"\"\"**IFRS ANSWER:** <font color=\"red\">{answer['output']}</font>\"\"\"))\n",
        "    ifrs_response: ResponseNodeState = {\"answer\": answer['output'],\n",
        "                                        \"metadata\": []}\n",
        "    return {\"ifrs_response\": ifrs_response}\n",
        "\n",
        "\n",
        "def auditor_guidance_answer_node(state):\n",
        "    \"\"\"Use this tool to answer audit related questions\"\"\"\n",
        "    print(\"------ENTERING: AUDITOR GUIDANCE ANSWER NODE------\")\n",
        "    tools = [AUDIT_tool]\n",
        "    generate_agent = create_qa_agent(llm, tools, KPMG_EY_PwC_prompt, verbose=False)\n",
        "    with get_openai_callback() as cb:\n",
        "        answer = generate_agent.invoke({\"input\":state['question']})\n",
        "\n",
        "    display(Markdown(f\"\"\"**IFRS ANSWER:** <font color=\"red\">{answer['output']}</font>\"\"\"))\n",
        "    audit_response: ResponseNodeState = {\"answer\": answer['output'],\n",
        "                                        \"metadata\": []}\n",
        "    return {\"audit_response\": audit_response}\n",
        "\n",
        "\n",
        "def annual_reports_answer_node(state):\n",
        "    \"\"\"Use this tool to answer annual reports related questions\"\"\"\n",
        "    print(\"------ENTERING: ANNUAL REPORTS ANSWER NODE------\")\n",
        "    all_competitors = ['Roche','GSK','Bayer','AstraZeneca','Sanofi', 'Amgen', 'Biogen', 'Abbvie', 'BMS/Bristol Myers Squibb', 'Gilead', 'Eli Lilly', 'Merck', 'Pfizer', 'Takeda','Johnson&Johnson', 'novo-nordisk']\n",
        "\n",
        "    competitors = ['Roche', 'Sanofi', 'Bayer', 'GSK', 'AstraZeneca']\n",
        "    web_tool = bing_search\n",
        "\n",
        "    tools = [ANNUAL_REPORTS_tool, web_tool]\n",
        "    generate_agent = create_qa_agent(llm, tools, AR_prompt, verbose=False)\n",
        "    with get_openai_callback() as cb:\n",
        "        answer = generate_agent.invoke({\"input\":state['question'], 'all_competitors':all_competitors, 'top5_competitors':competitors })\n",
        "    display(Markdown(f\"\"\"**ANNUAL REPORTS ANSWER:** <font color=\"red\">{answer['output']}</font>\"\"\"))\n",
        "    annual_reports_response: ResponseNodeState = {\"answer\": answer['output'],\n",
        "                                                    \"metadata\": []}\n",
        "    return {\"annual_reports_response\": annual_reports_response}\n",
        "\n",
        "\n",
        "def get_unified_response(_llm, unified_response_prompt, all_answers):\n",
        "    with get_openai_callback() as cb:\n",
        "        unified_response = _llm.invoke(unified_response_prompt.format(all_answers=all_answers))\n",
        "    return unified_response.content\n",
        "\n",
        "\n",
        "def unified_answer_node(state):\n",
        "    \"\"\"Use this tool to consolidate and give a unified answer\"\"\"\n",
        "    print(\"------ENTERING: UNIFIED ANSWER NODE------\")\n",
        "    display(JSON(state))\n",
        "    all_answers = \"\"\n",
        "    node_response_dict = {\"ifrs_answer_node\": [\"### IFRS: \", \"ifrs_response\"],\n",
        "                             \"annual_reports_answer_node\": [\"### Annual Reports: \", \"annual_reports_response\"],\n",
        "                             \"fm_answer_node\": [\"### Foundational ChatGPT: \", \"fm_response\"]}\n",
        "\n",
        "    for source in node_response_dict.keys():\n",
        "        if source in state['source_detector_check']['observation']:\n",
        "            all_answers = (\n",
        "                    all_answers\n",
        "                    + node_response_dict[source][0]\n",
        "                    + \"\\n\"\n",
        "                    + state[node_response_dict[source][1]][\"answer\"]\n",
        "                    + \"\\n\\n\"\n",
        "                    + \"---\"\n",
        "                    + \"\\n\\n\"\n",
        "                )\n",
        "\n",
        "    answer = get_unified_response(llm, unified_response_prompt, all_answers)\n",
        "    display(Markdown(f\"\"\"**UNIFIED ANSWER:** <font color=\"red\">{answer}</font>\"\"\"))\n",
        "\n",
        "    unified_response: ResponseNodeState = {\"answer\": answer,\n",
        "                                            \"metadata\": []}\n",
        "\n",
        "    all_answers = all_answers + \"### Unified Response\" +\"\\n\" +answer + \"\\n\\n\"\n",
        "\n",
        "    return {\"unified_response\": unified_response, \"final_answer\": all_answers}\n",
        "\n",
        "\n",
        "\n",
        "def overall_status_check_node(state):\n",
        "    \"\"\"Use this tool to check the overall status and update the config settings\"\"\"\n",
        "    print(\"------ENTERING: OVERALL STATUS CHECK NODE------\")\n",
        "    observation = \"Completed\"\n",
        "    overall_status_check: CheckNodeState = {\"observation\": observation}\n",
        "    print(\"-------------------------------- {} --------------------------------\".format(red(\"Final Answer\", ['bold'])))\n",
        "    display(Markdown(f\"\"\"**FINAL ANSWER:** <font color=\"red\">{state['final_answer']}</font>\"\"\"))\n",
        "\n",
        "    return {\"overall_status_check\": overall_status_check}"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "id": "d13fac97-df76-44e4-b313-279bbc8f7a06",
      "metadata": {
        "tags": [],
        "id": "d13fac97-df76-44e4-b313-279bbc8f7a06"
      },
      "outputs": [],
      "source": [
        "from langgraph.graph import StateGraph\n",
        "from typing_extensions import TypedDict\n",
        "from typing import Annotated, List\n",
        "from langchain_core.messages import AnyMessage\n",
        "import operator\n",
        "\n",
        "\n",
        "class GraphState(TypedDict):\n",
        "    \"\"\"\n",
        "    Represents the state of our graph.\n",
        "\n",
        "    Attributes:\n",
        "        question: question\n",
        "        finance_check: whether user question needs finance answer or generic answer\n",
        "        generic_response: generic answer\n",
        "        query_rerouter_check: whether user question needs web search or fra sources to answer\n",
        "        web_search: web answer\n",
        "        source_detector: List of fra sources applicable for answering the user question\n",
        "        ifrs_answer: ifrs answer\n",
        "        annual_reports_answer: annual reports answer\n",
        "        fm_answer: foundational model answer\n",
        "        unified_answer: consistency check and unified answer\n",
        "    \"\"\"\n",
        "\n",
        "    operation_id: int\n",
        "    user_id: str\n",
        "    question: str\n",
        "    topic: str\n",
        "    requested_datasources: List[str]\n",
        "    final_answer: Annotated[str, operator.add]\n",
        "\n",
        "    finance_check: CheckNodeState\n",
        "    query_rerouter_check: CheckNodeState\n",
        "    source_detector_check: SourceDetectNodeState\n",
        "    overall_status_check: CheckNodeState\n",
        "\n",
        "    generic_response: ResponseNodeState\n",
        "    human_response: ResponseNodeState\n",
        "    web_response: ResponseNodeState\n",
        "    ifrs_response: ResponseNodeState\n",
        "    annual_reports_response: ResponseNodeState\n",
        "    audit_response: ResponseNodeState\n",
        "    unified_response: ResponseNodeState\n",
        "    intermediate_steps: Annotated[list[AnyMessage], operator.add]\n",
        "\n",
        "\n",
        "\n",
        "## Main Graph\n",
        "\n",
        "builder = StateGraph(GraphState)\n",
        "builder.add_node(\"topic_modelling_node\", topic_modelling_node)\n",
        "builder.add_node(\"finance_check_node\", finance_check_node)\n",
        "builder.add_node(\"generic_response_node\", generic_response_node)\n",
        "builder.add_node(\"query_rerouter_node\", query_rerouter_node)\n",
        "builder.add_node(\"human_check_node\", human_check_node)\n",
        "builder.add_node(\"web_search_node\", web_search_node)\n",
        "builder.add_node(\"source_detector_node\", source_detector_node)\n",
        "builder.add_node(\"ifrs_answer_node\", ifrs_answer_node)\n",
        "builder.add_node(\"annual_reports_answer_node\", annual_reports_answer_node)\n",
        "builder.add_node(\"auditor_guidance_answer_node\", auditor_guidance_answer_node)\n",
        "builder.add_node(\"unified_answer_node\", unified_answer_node)\n",
        "builder.add_node(\"overall_status_check_node\", overall_status_check_node)\n",
        "\n",
        "builder.set_entry_point(\"topic_modelling_node\")\n",
        "builder.add_edge(\"topic_modelling_node\", \"finance_check_node\")\n",
        "\n",
        "def finance_check_edge(state):\n",
        "    finance_check = state[\"finance_check\"]\n",
        "\n",
        "    if finance_check['observation'] == \"Yes\":\n",
        "        print(\"------DECISION: INVOKE QUERY REROUTER NODE------\")\n",
        "        return \"query_rerouter_node\"\n",
        "    else:\n",
        "        print(\"------DECISION: INVOKE GENERIC RESPONSE NODE------\")\n",
        "        return \"generic_response_node\"\n",
        "\n",
        "\n",
        "finance_check_possible_nodes = [\"query_rerouter_node\", \"generic_response_node\"]\n",
        "builder.add_conditional_edges(\"finance_check_node\", finance_check_edge, finance_check_possible_nodes)\n",
        "builder.add_edge(\"generic_response_node\", \"overall_status_check_node\")\n",
        "\n",
        "\n",
        "def query_rerouter_edge(state):\n",
        "    query_rerouter_check = state[\"query_rerouter_check\"]\n",
        "\n",
        "    if query_rerouter_check['observation'] == \"FRA\":\n",
        "        print(\"------DECISION: INVOKE SOURCE DETECTOR NODE------\")\n",
        "        return \"source_detector_node\"\n",
        "    else:\n",
        "        print(\"------DECISION: CHECK WITH USER TO INVOKE WEB SEARCH NODE------\")\n",
        "        return \"human_check_node\"\n",
        "\n",
        "\n",
        "query_rerouter_possible_nodes = [\"human_check_node\", \"source_detector_node\"]\n",
        "builder.add_conditional_edges(\"query_rerouter_node\", query_rerouter_edge, query_rerouter_possible_nodes)\n",
        "\n",
        "\n",
        "def human_check_edge(state):\n",
        "    if state['human_response']['answer'] == \"yes\":\n",
        "        print(\"------DECISION: INVOKE WEB SEARCH NODE------\")\n",
        "        return \"web_search_node\"\n",
        "    else:\n",
        "        print(\"------Your question cannot be answered due to lack of information from private data sources, please ask a different question!------\")\n",
        "        return \"overall_status_check_node\"\n",
        "\n",
        "\n",
        "builder.add_conditional_edges(\"human_check_node\", human_check_edge, [\"web_search_node\", \"overall_status_check_node\"])\n",
        "\n",
        "builder.add_edge(\"web_search_node\", \"overall_status_check_node\")\n",
        "\n",
        "\n",
        "def source_detector_edge(state) -> list:\n",
        "    return state[\"source_detector_check\"]['observation']\n",
        "\n",
        "\n",
        "individual_answer_nodes = [\"annual_reports_answer_node\", \"ifrs_answer_node\", \"auditor_guidance_answer_node\"]\n",
        "builder.add_conditional_edges(\"source_detector_node\", source_detector_edge, individual_answer_nodes)\n",
        "\n",
        "for node in individual_answer_nodes:\n",
        "    builder.add_edge(node, \"unified_answer_node\")\n",
        "\n",
        "\n",
        "builder.add_edge(\"unified_answer_node\", \"overall_status_check_node\")\n",
        "builder.set_finish_point(\"overall_status_check_node\")\n",
        "\n",
        "memory = SqliteSaver.from_conn_string(\":memory:\")\n",
        "graph = builder.compile()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "id": "a04f9819-b5eb-4c89-9987-7907b712e951",
      "metadata": {
        "tags": [],
        "id": "a04f9819-b5eb-4c89-9987-7907b712e951",
        "outputId": "ffd3f95d-50a4-4dde-a94e-0ee43ed18b23",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 741
        }
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/jpeg": "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\n",
            "text/plain": [
              "<IPython.core.display.Image object>"
            ]
          },
          "metadata": {}
        }
      ],
      "source": [
        "from IPython.display import Image, display\n",
        "\n",
        "display(Image(graph.get_graph().draw_mermaid_png()))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "id": "969ea3bb-4b84-45a5-b1e5-41f2225e365e",
      "metadata": {
        "tags": [],
        "id": "969ea3bb-4b84-45a5-b1e5-41f2225e365e"
      },
      "outputs": [],
      "source": [
        "import time\n",
        "from simple_colors import *\n",
        "\n",
        "def run_answer(question, t):\n",
        "    inputs = {\"question\": question, \"operation_id\": 123456, \"user_id\":\"nalabsr1\"}\n",
        "    thread = {\"configurable\": {\"thread_id\": str(t)}}\n",
        "    start_time = time.time()\n",
        "    for output in graph.stream(inputs, thread, stream_mode='values'):\n",
        "#         print(blue(output, ['bold']))\n",
        "        pass\n",
        "    ex_time = time.time() - start_time\n",
        "    print(\"--------------------------------------------------------\")\n",
        "    print(red(f\"Total Time Taken - [{round(ex_time, 2)}]\", ['bold']))\n",
        "    print(\"--------------------------------------------------------\")\n",
        "    return"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "id": "093f9654-f3f0-4378-9930-7f87f6889470",
      "metadata": {
        "tags": [],
        "id": "093f9654-f3f0-4378-9930-7f87f6889470",
        "outputId": "24dd6911-a778-4efb-c2e1-70bc6bdfc795",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 732
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "------ENTERING: TOPIC MODELLING NODE------\n",
            "============================================\n",
            "{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'What is the income of bayer in 2024 Q1?', 'topic': None, 'requested_datasources': None, 'final_answer': '', 'finance_check': None, 'query_rerouter_check': None, 'source_detector_check': None, 'overall_status_check': None, 'generic_response': None, 'human_response': None, 'web_response': None, 'ifrs_response': None, 'annual_reports_response': None, 'audit_response': None, 'unified_response': None, 'intermediate_steps': []}\n",
            "============================================\n",
            "------OBSERVATION: DUMMY TOPIC------\n",
            "------ENTERING: FINANCE CHECK NODE------\n",
            "------OBSERVATION: Yes------\n",
            "------DECISION: INVOKE QUERY REROUTER NODE------\n",
            "------ENTERING: QUERY REROUTER NODE------\n",
            "------OBSERVATION: WEB------\n",
            "------DECISION: CHECK WITH USER TO INVOKE WEB SEARCH NODE------\n",
            "The answer is not available from the private data sources! Do you want me to search over the internet to answer?Yes\n",
            "------DECISION: INVOKE WEB SEARCH NODE------\n",
            "------ENTERING: WEB SEARCH NODE------\n",
            "------WEB SEARCH ANSWER: I was unable to retrieve the detailed content from the provided links. However, based on the search snippets, here is the relevant information regarding Bayer's income for Q1 2024:\n",
            "\n",
            "- **Group Sales**: €13.765 billion\n",
            "- **EBITDA before special items**: €4.412 billion\n",
            "- **Currency headwinds**: €525 million\n",
            "- **Change in Group Sales**: -0.6% on a currency- and portfolio-adjusted basis, and -4.3% on a reported basis.\n",
            "\n",
            "For more detailed information, you can visit the [Bayer AG First Quarter 2024 Results and Media Update](https://www.bayer.com/media/en-us/bayer-ag-first-quarter-2024-results-and-media-update/) or the [Q1 2024 Results | Bayer Global](https://www.bayer.com/en/investors/q1-2024-investor-video-call).\n",
            "\n",
            "If you need further details, I recommend checking the official quarterly statement directly from Bayer's investor relations page.------\n",
            "------ENTERING: OVERALL STATUS CHECK NODE------\n",
            "-------------------------------- \u001b[1;31mFinal Answer\u001b[0m --------------------------------\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ],
            "text/markdown": "**FINAL ANSWER:** <font color=\"red\">I was unable to retrieve the detailed content from the provided links. However, based on the search snippets, here is the relevant information regarding Bayer's income for Q1 2024:\n\n- **Group Sales**: €13.765 billion\n- **EBITDA before special items**: €4.412 billion\n- **Currency headwinds**: €525 million\n- **Change in Group Sales**: -0.6% on a currency- and portfolio-adjusted basis, and -4.3% on a reported basis.\n\nFor more detailed information, you can visit the [Bayer AG First Quarter 2024 Results and Media Update](https://www.bayer.com/media/en-us/bayer-ag-first-quarter-2024-results-and-media-update/) or the [Q1 2024 Results | Bayer Global](https://www.bayer.com/en/investors/q1-2024-investor-video-call).\n\nIf you need further details, I recommend checking the official quarterly statement directly from Bayer's investor relations page.</font>"
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--------------------------------------------------------\n",
            "\u001b[1;31mTotal Time Taken - [22.87]\u001b[0m\n",
            "--------------------------------------------------------\n"
          ]
        }
      ],
      "source": [
        "question = \"What is the income of bayer in 2024 Q1?\"\n",
        "run_answer(question, 89)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "b02e06eb-1327-43c3-9108-d8cb1471bc4b",
      "metadata": {
        "tags": [],
        "id": "b02e06eb-1327-43c3-9108-d8cb1471bc4b",
        "outputId": "8dfeb536-72af-44af-ba6d-943ede94e18c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 584
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "------ENTERING: TOPIC MODELLING NODE------\n",
            "============================================\n",
            "{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'What is the guidance for identifying a lease as per IFRS?', 'topic': None, 'requested_datasources': None, 'final_answer': '', 'finance_check': None, 'query_rerouter_check': None, 'source_detector_check': None, 'overall_status_check': None, 'generic_response': None, 'human_response': None, 'web_response': None, 'ifrs_response': None, 'annual_reports_response': None, 'audit_response': None, 'unified_response': None, 'intermediate_steps': []}\n",
            "============================================\n",
            "------OBSERVATION: DUMMY TOPIC------\n",
            "------ENTERING: FINANCE CHECK NODE------\n",
            "------OBSERVATION: Yes------\n",
            "------DECISION: INVOKE QUERY REROUTER NODE------\n",
            "------ENTERING: QUERY REROUTER NODE------\n",
            "------OBSERVATION: FRA------\n",
            "------DECISION: INVOKE SOURCE DETECTOR NODE------\n",
            "------ENTERING: SOURCE DETECTOR NODE------\n",
            "['ifrs_answer_node']\n",
            "------SOURCES DETECTED: ['ifrs_answer_node']------\n",
            "------ENTERING: IFRS ANSWER NODE------\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "OperationalError",
          "evalue": "unable to open database file",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mOperationalError\u001b[0m                          Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-50-c9342550fa1a>\u001b[0m in \u001b[0;36m<cell line: 2>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mquestion\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"What is the guidance for identifying a lease as per IFRS?\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mrun_answer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mquestion\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m89\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-47-ede8da42c920>\u001b[0m in \u001b[0;36mrun_answer\u001b[0;34m(question, t)\u001b[0m\n\u001b[1;32m      6\u001b[0m     \u001b[0mthread\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m\"configurable\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m\"thread_id\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m     \u001b[0mstart_time\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 8\u001b[0;31m     \u001b[0;32mfor\u001b[0m \u001b[0moutput\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mgraph\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstream\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minputs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mthread\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstream_mode\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'values'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      9\u001b[0m \u001b[0;31m#         print(blue(output, ['bold']))\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m         \u001b[0;32mpass\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langgraph/pregel/__init__.py\u001b[0m in \u001b[0;36mstream\u001b[0;34m(self, input, config, stream_mode, output_keys, input_keys, interrupt_before, interrupt_after, debug)\u001b[0m\n\u001b[1;32m    874\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    875\u001b[0m                     \u001b[0;31m# panic on failure or timeout\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 876\u001b[0;31m                     \u001b[0m_panic_or_proceed\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minflight\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstep\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    877\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    878\u001b[0m                     \u001b[0;31m# combine pending writes from all tasks\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langgraph/pregel/__init__.py\u001b[0m in \u001b[0;36m_panic_or_proceed\u001b[0;34m(done, inflight, step)\u001b[0m\n\u001b[1;32m   1420\u001b[0m                 \u001b[0minflight\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpop\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcancel\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1421\u001b[0m             \u001b[0;31m# raise the exception\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1422\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mexc\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1423\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1424\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0minflight\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/concurrent/futures/thread.py\u001b[0m in \u001b[0;36mrun\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     56\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 58\u001b[0;31m             \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     59\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mBaseException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mexc\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     60\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfuture\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mset_exception\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mexc\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langgraph/pregel/retry.py\u001b[0m in \u001b[0;36mrun_with_retry\u001b[0;34m(task, retry_policy)\u001b[0m\n\u001b[1;32m     64\u001b[0m             \u001b[0mtask\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwrites\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclear\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m             \u001b[0;31m# run the task\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 66\u001b[0;31m             \u001b[0mtask\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mproc\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minvoke\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtask\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtask\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconfig\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     67\u001b[0m             \u001b[0;31m# if successful, end\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     68\u001b[0m             \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain_core/runnables/base.py\u001b[0m in \u001b[0;36minvoke\u001b[0;34m(self, input, config, **kwargs)\u001b[0m\n\u001b[1;32m   2871\u001b[0m                 )\n\u001b[1;32m   2872\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0mi\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2873\u001b[0;31m                     \u001b[0minput\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mstep\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minvoke\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2874\u001b[0m                 \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2875\u001b[0m                     \u001b[0minput\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mstep\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minvoke\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langgraph/utils.py\u001b[0m in \u001b[0;36minvoke\u001b[0;34m(self, input, config)\u001b[0m\n\u001b[1;32m     87\u001b[0m                 \u001b[0;32melse\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     88\u001b[0m             )\n\u001b[0;32m---> 89\u001b[0;31m             \u001b[0mret\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcontext\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfunc\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     90\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mret\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mRunnable\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrecurse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     91\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mret\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minvoke\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-44-d9f71435d47b>\u001b[0m in \u001b[0;36mifrs_answer_node\u001b[0;34m(state)\u001b[0m\n\u001b[1;32m    239\u001b[0m     \u001b[0mgenerate_agent\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcreate_qa_agent\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mllm\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtools\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mIFRS_di_prompt\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mverbose\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    240\u001b[0m     \u001b[0;32mwith\u001b[0m \u001b[0mget_openai_callback\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mcb\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 241\u001b[0;31m         \u001b[0manswer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgenerate_agent\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minvoke\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m{\u001b[0m\u001b[0;34m\"input\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0mstate\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'question'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    242\u001b[0m     \u001b[0mdisplay\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mMarkdown\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"\"\"**IFRS ANSWER:** <font color=\"red\">{answer['output']}</font>\"\"\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    243\u001b[0m     ifrs_response: ResponseNodeState = {\"answer\": answer['output'],\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain/chains/base.py\u001b[0m in \u001b[0;36minvoke\u001b[0;34m(self, input, config, **kwargs)\u001b[0m\n\u001b[1;32m    164\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mBaseException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    165\u001b[0m             \u001b[0mrun_manager\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mon_chain_error\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 166\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    167\u001b[0m         \u001b[0mrun_manager\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mon_chain_end\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moutputs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    168\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain/chains/base.py\u001b[0m in \u001b[0;36minvoke\u001b[0;34m(self, input, config, **kwargs)\u001b[0m\n\u001b[1;32m    154\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_validate_inputs\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minputs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    155\u001b[0m             outputs = (\n\u001b[0;32m--> 156\u001b[0;31m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_call\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minputs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrun_manager\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mrun_manager\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    157\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0mnew_arg_supported\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    158\u001b[0m                 \u001b[0;32melse\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_call\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minputs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain/agents/agent.py\u001b[0m in \u001b[0;36m_call\u001b[0;34m(self, inputs, run_manager)\u001b[0m\n\u001b[1;32m   1634\u001b[0m         \u001b[0;31m# We now enter the agent loop (until it returns something).\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1635\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_should_continue\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0miterations\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtime_elapsed\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1636\u001b[0;31m             next_step_output = self._take_next_step(\n\u001b[0m\u001b[1;32m   1637\u001b[0m                 \u001b[0mname_to_tool_map\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1638\u001b[0m                 \u001b[0mcolor_mapping\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain/agents/agent.py\u001b[0m in \u001b[0;36m_take_next_step\u001b[0;34m(self, name_to_tool_map, color_mapping, inputs, intermediate_steps, run_manager)\u001b[0m\n\u001b[1;32m   1340\u001b[0m     ) -> Union[AgentFinish, List[Tuple[AgentAction, str]]]:\n\u001b[1;32m   1341\u001b[0m         return self._consume_next_step(\n\u001b[0;32m-> 1342\u001b[0;31m             [\n\u001b[0m\u001b[1;32m   1343\u001b[0m                 \u001b[0ma\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1344\u001b[0m                 for a in self._iter_next_step(\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain/agents/agent.py\u001b[0m in \u001b[0;36m<listcomp>\u001b[0;34m(.0)\u001b[0m\n\u001b[1;32m   1340\u001b[0m     ) -> Union[AgentFinish, List[Tuple[AgentAction, str]]]:\n\u001b[1;32m   1341\u001b[0m         return self._consume_next_step(\n\u001b[0;32m-> 1342\u001b[0;31m             [\n\u001b[0m\u001b[1;32m   1343\u001b[0m                 \u001b[0ma\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1344\u001b[0m                 for a in self._iter_next_step(\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain/agents/agent.py\u001b[0m in \u001b[0;36m_iter_next_step\u001b[0;34m(self, name_to_tool_map, color_mapping, inputs, intermediate_steps, run_manager)\u001b[0m\n\u001b[1;32m   1425\u001b[0m             \u001b[0;32myield\u001b[0m \u001b[0magent_action\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1426\u001b[0m         \u001b[0;32mfor\u001b[0m \u001b[0magent_action\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mactions\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1427\u001b[0;31m             yield self._perform_agent_action(\n\u001b[0m\u001b[1;32m   1428\u001b[0m                 \u001b[0mname_to_tool_map\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcolor_mapping\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0magent_action\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrun_manager\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1429\u001b[0m             )\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain/agents/agent.py\u001b[0m in \u001b[0;36m_perform_agent_action\u001b[0;34m(self, name_to_tool_map, color_mapping, agent_action, run_manager)\u001b[0m\n\u001b[1;32m   1447\u001b[0m                 \u001b[0mtool_run_kwargs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"llm_prefix\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1448\u001b[0m             \u001b[0;31m# We then call the tool on the tool input to get an observation\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1449\u001b[0;31m             observation = tool.run(\n\u001b[0m\u001b[1;32m   1450\u001b[0m                 \u001b[0magent_action\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtool_input\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1451\u001b[0m                 \u001b[0mverbose\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mverbose\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain_core/tools.py\u001b[0m in \u001b[0;36mrun\u001b[0;34m(self, tool_input, verbose, start_color, color, callbacks, tags, metadata, run_name, run_id, config, tool_call_id, **kwargs)\u001b[0m\n\u001b[1;32m    632\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0merror_to_raise\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    633\u001b[0m             \u001b[0mrun_manager\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mon_tool_error\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0merror_to_raise\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 634\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0merror_to_raise\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    635\u001b[0m         \u001b[0moutput\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_format_output\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcontent\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0martifact\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtool_call_id\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    636\u001b[0m         \u001b[0mrun_manager\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mon_tool_end\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moutput\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcolor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcolor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain_core/tools.py\u001b[0m in \u001b[0;36mrun\u001b[0;34m(self, tool_input, verbose, start_color, color, callbacks, tags, metadata, run_name, run_id, config, tool_call_id, **kwargs)\u001b[0m\n\u001b[1;32m    605\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mconfig_param\u001b[0m \u001b[0;34m:=\u001b[0m \u001b[0m_get_runnable_config_param\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_run\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    606\u001b[0m                 \u001b[0mtool_kwargs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mconfig_param\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 607\u001b[0;31m             \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcontext\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_run\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0mtool_args\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mtool_kwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    608\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mresponse_format\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"content_and_artifact\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    609\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtuple\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;36m2\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain_core/tools.py\u001b[0m in \u001b[0;36m_run\u001b[0;34m(self, config, run_manager, *args, **kwargs)\u001b[0m\n\u001b[1;32m    820\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mconfig_param\u001b[0m \u001b[0;34m:=\u001b[0m \u001b[0m_get_runnable_config_param\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfunc\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    821\u001b[0m                 \u001b[0mkwargs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mconfig_param\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 822\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    823\u001b[0m         \u001b[0;32mraise\u001b[0m \u001b[0mNotImplementedError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Tool does not support sync invocation.\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    824\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain_core/tools.py\u001b[0m in \u001b[0;36m_get_relevant_documents\u001b[0;34m(query, retriever, document_prompt, document_separator, callbacks)\u001b[0m\n\u001b[1;32m   1299\u001b[0m     \u001b[0mcallbacks\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mCallbacks\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1300\u001b[0m ) -> str:\n\u001b[0;32m-> 1301\u001b[0;31m     \u001b[0mdocs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mretriever\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minvoke\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mquery\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconfig\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m{\u001b[0m\u001b[0;34m\"callbacks\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mcallbacks\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1302\u001b[0m     return document_separator.join(\n\u001b[1;32m   1303\u001b[0m         \u001b[0mformat_document\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdoc\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdocument_prompt\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mdoc\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mdocs\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain_core/retrievers.py\u001b[0m in \u001b[0;36minvoke\u001b[0;34m(self, input, config, **kwargs)\u001b[0m\n\u001b[1;32m    219\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    220\u001b[0m             \u001b[0mrun_manager\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mon_retriever_error\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 221\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    222\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    223\u001b[0m             run_manager.on_retriever_end(\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain_core/retrievers.py\u001b[0m in \u001b[0;36minvoke\u001b[0;34m(self, input, config, **kwargs)\u001b[0m\n\u001b[1;32m    212\u001b[0m             \u001b[0m_kwargs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mkwargs\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_expects_other_args\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    213\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_new_arg_supported\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 214\u001b[0;31m                 result = self._get_relevant_documents(\n\u001b[0m\u001b[1;32m    215\u001b[0m                     \u001b[0minput\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrun_manager\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mrun_manager\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0m_kwargs\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    216\u001b[0m                 )\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain/retrievers/multi_vector.py\u001b[0m in \u001b[0;36m_get_relevant_documents\u001b[0;34m(self, query, run_manager)\u001b[0m\n\u001b[1;32m     75\u001b[0m             \u001b[0msub_docs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0msub_doc\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0msub_doc\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_\u001b[0m \u001b[0;32min\u001b[0m \u001b[0msub_docs_and_similarities\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     76\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 77\u001b[0;31m             \u001b[0msub_docs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvectorstore\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msimilarity_search\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mquery\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msearch_kwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     78\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     79\u001b[0m         \u001b[0;31m# We do this to maintain the order of the ids that are returned\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain_chroma/vectorstores.py\u001b[0m in \u001b[0;36msimilarity_search\u001b[0;34m(self, query, k, filter, **kwargs)\u001b[0m\n\u001b[1;32m    461\u001b[0m             \u001b[0mList\u001b[0m \u001b[0mof\u001b[0m \u001b[0mdocuments\u001b[0m \u001b[0mmost\u001b[0m \u001b[0msimilar\u001b[0m \u001b[0mto\u001b[0m \u001b[0mthe\u001b[0m \u001b[0mquery\u001b[0m \u001b[0mtext\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    462\u001b[0m         \"\"\"\n\u001b[0;32m--> 463\u001b[0;31m         docs_and_scores = self.similarity_search_with_score(\n\u001b[0m\u001b[1;32m    464\u001b[0m             \u001b[0mquery\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mk\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfilter\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfilter\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    465\u001b[0m         )\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain_chroma/vectorstores.py\u001b[0m in \u001b[0;36msimilarity_search_with_score\u001b[0;34m(self, query, k, filter, where_document, **kwargs)\u001b[0m\n\u001b[1;32m    559\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    560\u001b[0m             \u001b[0mquery_embedding\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_embedding_function\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0membed_query\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mquery\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 561\u001b[0;31m             results = self.__query_collection(\n\u001b[0m\u001b[1;32m    562\u001b[0m                 \u001b[0mquery_embeddings\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mquery_embedding\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    563\u001b[0m                 \u001b[0mn_results\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mk\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain_core/utils/utils.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m     45\u001b[0m                     \u001b[0;34mf\" {', '.join(invalid_group_names)}\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     46\u001b[0m                 )\n\u001b[0;32m---> 47\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     48\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     49\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mwrapper\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/langchain_chroma/vectorstores.py\u001b[0m in \u001b[0;36m__query_collection\u001b[0;34m(self, query_texts, query_embeddings, n_results, where, where_document, **kwargs)\u001b[0m\n\u001b[1;32m    258\u001b[0m         \u001b[0mSee\u001b[0m \u001b[0mmore\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mhttps\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m//\u001b[0m\u001b[0mdocs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtrychroma\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcom\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0mreference\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0mpy\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mcollection\u001b[0m\u001b[0;31m#query\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    259\u001b[0m         \"\"\"\n\u001b[0;32m--> 260\u001b[0;31m         return self._collection.query(\n\u001b[0m\u001b[1;32m    261\u001b[0m             \u001b[0mquery_texts\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mquery_texts\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    262\u001b[0m             \u001b[0mquery_embeddings\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mquery_embeddings\u001b[0m\u001b[0;34m,\u001b[0m  \u001b[0;31m# type: ignore\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/chromadb/api/models/Collection.py\u001b[0m in \u001b[0;36mquery\u001b[0;34m(self, query_embeddings, query_texts, n_results, where, where_document, include)\u001b[0m\n\u001b[1;32m    219\u001b[0m             \u001b[0mwhere_document\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    220\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 221\u001b[0;31m         return self._client._query(\n\u001b[0m\u001b[1;32m    222\u001b[0m             \u001b[0mcollection_id\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mid\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    223\u001b[0m             \u001b[0mquery_embeddings\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mquery_embeddings\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/chromadb/telemetry/opentelemetry/__init__.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    125\u001b[0m             \u001b[0;32mglobal\u001b[0m \u001b[0mtracer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mgranularity\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    126\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mtrace_granularity\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mgranularity\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 127\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    128\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mtracer\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    129\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/chromadb/api/segment.py\u001b[0m in \u001b[0;36m_query\u001b[0;34m(self, collection_id, query_embeddings, n_results, where, where_document, include)\u001b[0m\n\u001b[1;32m    594\u001b[0m         \u001b[0mallowed_ids\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    595\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 596\u001b[0;31m         \u001b[0mcoll\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_get_collection\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcollection_id\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    597\u001b[0m         \u001b[0;32mfor\u001b[0m \u001b[0membedding\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mquery_embeddings\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    598\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_validate_dimension\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcoll\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0membedding\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mupdate\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/chromadb/telemetry/opentelemetry/__init__.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    125\u001b[0m             \u001b[0;32mglobal\u001b[0m \u001b[0mtracer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mgranularity\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    126\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mtrace_granularity\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mgranularity\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 127\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    128\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mtracer\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    129\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/chromadb/api/segment.py\u001b[0m in \u001b[0;36m_get_collection\u001b[0;34m(self, collection_id)\u001b[0m\n\u001b[1;32m    739\u001b[0m         \u001b[0;34m\"\"\"Read-through cache for collection data\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    740\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mcollection_id\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_collection_cache\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 741\u001b[0;31m             \u001b[0mcollections\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_sysdb\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_collections\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mid\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcollection_id\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    742\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mcollections\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    743\u001b[0m                 raise InvalidCollectionException(\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/chromadb/telemetry/opentelemetry/__init__.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    125\u001b[0m             \u001b[0;32mglobal\u001b[0m \u001b[0mtracer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mgranularity\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    126\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mtrace_granularity\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mgranularity\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 127\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    128\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mtracer\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    129\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/chromadb/db/mixins/sysdb.py\u001b[0m in \u001b[0;36mget_collections\u001b[0;34m(self, id, topic, name, tenant, database)\u001b[0m\n\u001b[1;32m    415\u001b[0m             )\n\u001b[1;32m    416\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 417\u001b[0;31m         \u001b[0;32mwith\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtx\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mcur\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    418\u001b[0m             \u001b[0msql\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mget_sql\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mq\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mparameter_format\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    419\u001b[0m             \u001b[0mrows\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcur\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msql\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfetchall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/chromadb/db/impl/sqlite.py\u001b[0m in \u001b[0;36mtx\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    128\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mhasattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_tx_stack\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"stack\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    129\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_tx_stack\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstack\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 130\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mTxWrapper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_conn_pool\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstack\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_tx_stack\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    131\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    132\u001b[0m     \u001b[0;34m@\u001b[0m\u001b[0mtrace_method\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"SqliteDB.reset_state\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mOpenTelemetryGranularity\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mALL\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/chromadb/db/impl/sqlite.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, conn_pool, stack)\u001b[0m\n\u001b[1;32m     29\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconn_pool\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mPool\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstack\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mlocal\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     30\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_tx_stack\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mstack\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 31\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_conn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconn_pool\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     32\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_pool\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconn_pool\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     33\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/chromadb/db/impl/sqlite_pool.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m    139\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_connection\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconn\u001b[0m  \u001b[0;31m# type: ignore # cast doesn't work here for some reason\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    140\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 141\u001b[0;31m             new_connection = Connection(\n\u001b[0m\u001b[1;32m    142\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_db_file\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_is_uri\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    143\u001b[0m             )\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/chromadb/db/impl/sqlite_pool.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, pool, db_file, is_uri, *args, **kwargs)\u001b[0m\n\u001b[1;32m     18\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_pool\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_db_file\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdb_file\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m         self._conn = sqlite3.connect(\n\u001b[0m\u001b[1;32m     21\u001b[0m             \u001b[0mdb_file\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1000\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcheck_same_thread\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muri\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mis_uri\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m         )  # type: ignore\n",
            "\u001b[0;31mOperationalError\u001b[0m: unable to open database file"
          ]
        }
      ],
      "source": [
        "question = \"What is the guidance for identifying a lease as per IFRS?\"\n",
        "run_answer(question, 89)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "6e9ceacb-acf1-42b5-84c3-fcc41409b9d3",
      "metadata": {
        "tags": [],
        "id": "6e9ceacb-acf1-42b5-84c3-fcc41409b9d3",
        "outputId": "810ce803-69d7-4b11-ee52-3ea1bb10c7ee"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'How do I account for Gains on sales of fixed assets?', 'final_answer': '', 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: TOPIC MODELLING NODE------\n",
            "============================================\n",
            "{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'How do I account for Gains on sales of fixed assets?', 'topic': None, 'requested_datasources': None, 'final_answer': '', 'finance_check': None, 'query_rerouter_check': None, 'source_detector_check': None, 'overall_status_check': None, 'generic_response': None, 'web_response': None, 'ifrs_response': None, 'annual_reports_response': None, 'fm_response': None, 'unified_response': None, 'intermediate_steps': []}\n",
            "============================================\n",
            "------OBSERVATION: DUMMY TOPIC------\n",
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'How do I account for Gains on sales of fixed assets?', 'topic': 'DUMMY TOPIC', 'final_answer': '', 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: FINANCE CHECK NODE------\n",
            "------OBSERVATION: Yes------\n",
            "------DECISION: INVOKE QUERY REROUTER NODE------\n",
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'How do I account for Gains on sales of fixed assets?', 'topic': 'DUMMY TOPIC', 'final_answer': '', 'finance_check': {'observation': 'Yes'}, 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: QUERY REROUTER NODE------\n",
            "------OBSERVATION: FRA------\n",
            "------DECISION: INVOKE SOURCE DETECTOR NODE------\n",
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'How do I account for Gains on sales of fixed assets?', 'topic': 'DUMMY TOPIC', 'final_answer': '', 'finance_check': {'observation': 'Yes'}, 'query_rerouter_check': {'observation': 'FRA'}, 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: SOURCE DETECTOR NODE------\n",
            "------SOURCES DETECTED: ['annual_reports_answer_node', 'fm_answer_node', 'ifrs_answer_node']------\n",
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'How do I account for Gains on sales of fixed assets?', 'topic': 'DUMMY TOPIC', 'final_answer': '', 'finance_check': {'observation': 'Yes'}, 'query_rerouter_check': {'observation': 'FRA'}, 'source_detector_check': {'observation': ['annual_reports_answer_node', 'fm_answer_node', 'ifrs_answer_node']}, 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: IFRS ANSWER NODE------\n",
            "------ENTERING: ANNUAL REPORTS ANSWER NODE------\n",
            "------ENTERING: FOUNDATIONAL ANSWER NODE------\n"
          ]
        },
        {
          "data": {
            "text/markdown": [
              "**IFRS ANSWER:** <font color=\"red\">As per IAS 16, gains on the sale of fixed assets (property, plant, and equipment) should be accounted for as follows:\n",
              "\n",
              "- **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (paragraph 67-72).\n",
              "- **Recognition of Gain or Loss**: Any gain or loss arising from the derecognition of the asset should be recognized in profit or loss. This gain or loss is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (paragraph 71).\n",
              "\n",
              "Therefore, the gain on the sale of fixed assets should be recognized in the profit or loss statement at the date of derecognition.</font>"
            ],
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/markdown": [
              "**FOUNDATIONAL ANSWER:** <font color=\"red\">To account for gains on the sale of fixed assets, you need to follow the guidance provided by IAS 16 \"Property, Plant and Equipment\" and IFRS 5 \"Non-current Assets Held for Sale and Discontinued Operations\" if applicable.\n",
              "\n",
              "### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\n",
              "\n",
              "1. **Determine the Carrying Amount:**\n",
              "   - The carrying amount of the fixed asset is its cost less any accumulated depreciation and any accumulated impairment losses (IAS 16.6).\n",
              "\n",
              "2. **Calculate the Gain:**\n",
              "   - The gain on the sale of a fixed asset is calculated as the difference between the net disposal proceeds and the carrying amount of the asset at the time of sale (IAS 16.71).\n",
              "\n",
              "3. **Recognize the Gain:**\n",
              "   - The gain should be recognized in profit or loss when the asset is derecognized (IAS 16.68). Derecognition occurs when the asset is disposed of or when no future economic benefits are expected from its use or disposal (IAS 16.67).\n",
              "\n",
              "4. **Presentation in Financial Statements:**\n",
              "   - Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\n",
              "\n",
              "### Example Journal Entry:\n",
              "Assume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\n",
              "\n",
              "- **Journal Entry:**\n",
              "  - Debit: Cash/Bank $70,000\n",
              "  - Credit: Fixed Asset $50,000\n",
              "  - Credit: Gain on Sale of Fixed Asset $20,000\n",
              "\n",
              "### Relevant IFRS/IAS Paragraphs:\n",
              "- **IAS 16.6:** Definition of carrying amount.\n",
              "- **IAS 16.67:** Derecognition of an asset.\n",
              "- **IAS 16.68:** Recognition of gain or loss on derecognition.\n",
              "- **IAS 16.71:** Calculation of gain or loss on disposal.\n",
              "- **IAS 1.97:** Presentation of gains in the income statement.\n",
              "\n",
              "### Sources:\n",
              "- IAS 16 \"Property, Plant and Equipment\"\n",
              "- IAS 1 \"Presentation of Financial Statements\"\n",
              "\n",
              "By following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.</font>"
            ],
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/markdown": [
              "**ANNUAL REPORTS ANSWER:** <font color=\"red\">NO GUIDANCE</font>"
            ],
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'How do I account for Gains on sales of fixed assets?', 'topic': 'DUMMY TOPIC', 'final_answer': '', 'finance_check': {'observation': 'Yes'}, 'query_rerouter_check': {'observation': 'FRA'}, 'source_detector_check': {'observation': ['annual_reports_answer_node', 'fm_answer_node', 'ifrs_answer_node']}, 'ifrs_response': {'answer': 'As per IAS 16, gains on the sale of fixed assets (property, plant, and equipment) should be accounted for as follows:\\n\\n- **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (paragraph 67-72).\\n- **Recognition of Gain or Loss**: Any gain or loss arising from the derecognition of the asset should be recognized in profit or loss. This gain or loss is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (paragraph 71).\\n\\nTherefore, the gain on the sale of fixed assets should be recognized in the profit or loss statement at the date of derecognition.', 'metadata': []}, 'annual_reports_response': {'answer': 'NO GUIDANCE', 'metadata': []}, 'fm_response': {'answer': 'To account for gains on the sale of fixed assets, you need to follow the guidance provided by IAS 16 \"Property, Plant and Equipment\" and IFRS 5 \"Non-current Assets Held for Sale and Discontinued Operations\" if applicable.\\n\\n### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\\n\\n1. **Determine the Carrying Amount:**\\n   - The carrying amount of the fixed asset is its cost less any accumulated depreciation and any accumulated impairment losses (IAS 16.6).\\n\\n2. **Calculate the Gain:**\\n   - The gain on the sale of a fixed asset is calculated as the difference between the net disposal proceeds and the carrying amount of the asset at the time of sale (IAS 16.71).\\n\\n3. **Recognize the Gain:**\\n   - The gain should be recognized in profit or loss when the asset is derecognized (IAS 16.68). Derecognition occurs when the asset is disposed of or when no future economic benefits are expected from its use or disposal (IAS 16.67).\\n\\n4. **Presentation in Financial Statements:**\\n   - Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\\n\\n### Example Journal Entry:\\nAssume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\\n\\n- **Journal Entry:**\\n  - Debit: Cash/Bank $70,000\\n  - Credit: Fixed Asset $50,000\\n  - Credit: Gain on Sale of Fixed Asset $20,000\\n\\n### Relevant IFRS/IAS Paragraphs:\\n- **IAS 16.6:** Definition of carrying amount.\\n- **IAS 16.67:** Derecognition of an asset.\\n- **IAS 16.68:** Recognition of gain or loss on derecognition.\\n- **IAS 16.71:** Calculation of gain or loss on disposal.\\n- **IAS 1.97:** Presentation of gains in the income statement.\\n\\n### Sources:\\n- IAS 16 \"Property, Plant and Equipment\"\\n- IAS 1 \"Presentation of Financial Statements\"\\n\\nBy following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.', 'metadata': []}, 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: UNIFIED ANSWER NODE------\n"
          ]
        },
        {
          "data": {
            "application/json": {
              "annual_reports_response": {
                "answer": "NO GUIDANCE",
                "metadata": []
              },
              "final_answer": "",
              "finance_check": {
                "observation": "Yes"
              },
              "fm_response": {
                "answer": "To account for gains on the sale of fixed assets, you need to follow the guidance provided by IAS 16 \"Property, Plant and Equipment\" and IFRS 5 \"Non-current Assets Held for Sale and Discontinued Operations\" if applicable.\n\n### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\n\n1. **Determine the Carrying Amount:**\n   - The carrying amount of the fixed asset is its cost less any accumulated depreciation and any accumulated impairment losses (IAS 16.6).\n\n2. **Calculate the Gain:**\n   - The gain on the sale of a fixed asset is calculated as the difference between the net disposal proceeds and the carrying amount of the asset at the time of sale (IAS 16.71).\n\n3. **Recognize the Gain:**\n   - The gain should be recognized in profit or loss when the asset is derecognized (IAS 16.68). Derecognition occurs when the asset is disposed of or when no future economic benefits are expected from its use or disposal (IAS 16.67).\n\n4. **Presentation in Financial Statements:**\n   - Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\n\n### Example Journal Entry:\nAssume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\n\n- **Journal Entry:**\n  - Debit: Cash/Bank $70,000\n  - Credit: Fixed Asset $50,000\n  - Credit: Gain on Sale of Fixed Asset $20,000\n\n### Relevant IFRS/IAS Paragraphs:\n- **IAS 16.6:** Definition of carrying amount.\n- **IAS 16.67:** Derecognition of an asset.\n- **IAS 16.68:** Recognition of gain or loss on derecognition.\n- **IAS 16.71:** Calculation of gain or loss on disposal.\n- **IAS 1.97:** Presentation of gains in the income statement.\n\n### Sources:\n- IAS 16 \"Property, Plant and Equipment\"\n- IAS 1 \"Presentation of Financial Statements\"\n\nBy following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.",
                "metadata": []
              },
              "generic_response": null,
              "ifrs_response": {
                "answer": "As per IAS 16, gains on the sale of fixed assets (property, plant, and equipment) should be accounted for as follows:\n\n- **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (paragraph 67-72).\n- **Recognition of Gain or Loss**: Any gain or loss arising from the derecognition of the asset should be recognized in profit or loss. This gain or loss is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (paragraph 71).\n\nTherefore, the gain on the sale of fixed assets should be recognized in the profit or loss statement at the date of derecognition.",
                "metadata": []
              },
              "intermediate_steps": [],
              "operation_id": 123456,
              "overall_status_check": null,
              "query_rerouter_check": {
                "observation": "FRA"
              },
              "question": "How do I account for Gains on sales of fixed assets?",
              "requested_datasources": null,
              "source_detector_check": {
                "observation": [
                  "annual_reports_answer_node",
                  "fm_answer_node",
                  "ifrs_answer_node"
                ]
              },
              "topic": "DUMMY TOPIC",
              "unified_response": null,
              "user_id": "nalabsr1",
              "web_response": null
            },
            "text/plain": [
              "<IPython.core.display.JSON object>"
            ]
          },
          "metadata": {
            "application/json": {
              "expanded": false,
              "root": "root"
            }
          },
          "output_type": "display_data"
        },
        {
          "data": {
            "text/markdown": [
              "**UNIFIED ANSWER:** <font color=\"red\">To account for gains on the sale of fixed assets, follow the guidance provided by IAS 16 \"Property, Plant, and Equipment.\"\n",
              "\n",
              "### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\n",
              "\n",
              "1. **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (IAS 16.67-72).\n",
              "2. **Calculate the Gain**: The gain is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (IAS 16.71).\n",
              "3. **Recognition of Gain**: Any gain arising from the derecognition of the asset should be recognized in profit or loss (IAS 16.68).\n",
              "4. **Presentation in Financial Statements**: Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\n",
              "\n",
              "### Example Journal Entry:\n",
              "Assume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\n",
              "\n",
              "- **Journal Entry:**\n",
              "  - Debit: Cash/Bank $70,000\n",
              "  - Credit: Fixed Asset $50,000\n",
              "  - Credit: Gain on Sale of Fixed Asset $20,000\n",
              "\n",
              "### Relevant IFRS/IAS Paragraphs:\n",
              "- **IAS 16.6**: Definition of carrying amount.\n",
              "- **IAS 16.67**: Derecognition of an asset.\n",
              "- **IAS 16.68**: Recognition of gain or loss on derecognition.\n",
              "- **IAS 16.71**: Calculation of gain or loss on disposal.\n",
              "- **IAS 1.97**: Presentation of gains in the income statement.\n",
              "\n",
              "By following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.</font>"
            ],
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'How do I account for Gains on sales of fixed assets?', 'topic': 'DUMMY TOPIC', 'final_answer': '### IFRS: \\nAs per IAS 16, gains on the sale of fixed assets (property, plant, and equipment) should be accounted for as follows:\\n\\n- **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (paragraph 67-72).\\n- **Recognition of Gain or Loss**: Any gain or loss arising from the derecognition of the asset should be recognized in profit or loss. This gain or loss is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (paragraph 71).\\n\\nTherefore, the gain on the sale of fixed assets should be recognized in the profit or loss statement at the date of derecognition.\\n\\n---\\n\\n### Annual Reports: \\nNO GUIDANCE\\n\\n---\\n\\n### Foundational ChatGPT: \\nTo account for gains on the sale of fixed assets, you need to follow the guidance provided by IAS 16 \"Property, Plant and Equipment\" and IFRS 5 \"Non-current Assets Held for Sale and Discontinued Operations\" if applicable.\\n\\n### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\\n\\n1. **Determine the Carrying Amount:**\\n   - The carrying amount of the fixed asset is its cost less any accumulated depreciation and any accumulated impairment losses (IAS 16.6).\\n\\n2. **Calculate the Gain:**\\n   - The gain on the sale of a fixed asset is calculated as the difference between the net disposal proceeds and the carrying amount of the asset at the time of sale (IAS 16.71).\\n\\n3. **Recognize the Gain:**\\n   - The gain should be recognized in profit or loss when the asset is derecognized (IAS 16.68). Derecognition occurs when the asset is disposed of or when no future economic benefits are expected from its use or disposal (IAS 16.67).\\n\\n4. **Presentation in Financial Statements:**\\n   - Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\\n\\n### Example Journal Entry:\\nAssume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\\n\\n- **Journal Entry:**\\n  - Debit: Cash/Bank $70,000\\n  - Credit: Fixed Asset $50,000\\n  - Credit: Gain on Sale of Fixed Asset $20,000\\n\\n### Relevant IFRS/IAS Paragraphs:\\n- **IAS 16.6:** Definition of carrying amount.\\n- **IAS 16.67:** Derecognition of an asset.\\n- **IAS 16.68:** Recognition of gain or loss on derecognition.\\n- **IAS 16.71:** Calculation of gain or loss on disposal.\\n- **IAS 1.97:** Presentation of gains in the income statement.\\n\\n### Sources:\\n- IAS 16 \"Property, Plant and Equipment\"\\n- IAS 1 \"Presentation of Financial Statements\"\\n\\nBy following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.\\n\\n---\\n\\n### Unified Response\\nTo account for gains on the sale of fixed assets, follow the guidance provided by IAS 16 \"Property, Plant, and Equipment.\"\\n\\n### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\\n\\n1. **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (IAS 16.67-72).\\n2. **Calculate the Gain**: The gain is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (IAS 16.71).\\n3. **Recognition of Gain**: Any gain arising from the derecognition of the asset should be recognized in profit or loss (IAS 16.68).\\n4. **Presentation in Financial Statements**: Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\\n\\n### Example Journal Entry:\\nAssume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\\n\\n- **Journal Entry:**\\n  - Debit: Cash/Bank $70,000\\n  - Credit: Fixed Asset $50,000\\n  - Credit: Gain on Sale of Fixed Asset $20,000\\n\\n### Relevant IFRS/IAS Paragraphs:\\n- **IAS 16.6**: Definition of carrying amount.\\n- **IAS 16.67**: Derecognition of an asset.\\n- **IAS 16.68**: Recognition of gain or loss on derecognition.\\n- **IAS 16.71**: Calculation of gain or loss on disposal.\\n- **IAS 1.97**: Presentation of gains in the income statement.\\n\\nBy following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.\\n\\n', 'finance_check': {'observation': 'Yes'}, 'query_rerouter_check': {'observation': 'FRA'}, 'source_detector_check': {'observation': ['annual_reports_answer_node', 'fm_answer_node', 'ifrs_answer_node']}, 'ifrs_response': {'answer': 'As per IAS 16, gains on the sale of fixed assets (property, plant, and equipment) should be accounted for as follows:\\n\\n- **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (paragraph 67-72).\\n- **Recognition of Gain or Loss**: Any gain or loss arising from the derecognition of the asset should be recognized in profit or loss. This gain or loss is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (paragraph 71).\\n\\nTherefore, the gain on the sale of fixed assets should be recognized in the profit or loss statement at the date of derecognition.', 'metadata': []}, 'annual_reports_response': {'answer': 'NO GUIDANCE', 'metadata': []}, 'fm_response': {'answer': 'To account for gains on the sale of fixed assets, you need to follow the guidance provided by IAS 16 \"Property, Plant and Equipment\" and IFRS 5 \"Non-current Assets Held for Sale and Discontinued Operations\" if applicable.\\n\\n### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\\n\\n1. **Determine the Carrying Amount:**\\n   - The carrying amount of the fixed asset is its cost less any accumulated depreciation and any accumulated impairment losses (IAS 16.6).\\n\\n2. **Calculate the Gain:**\\n   - The gain on the sale of a fixed asset is calculated as the difference between the net disposal proceeds and the carrying amount of the asset at the time of sale (IAS 16.71).\\n\\n3. **Recognize the Gain:**\\n   - The gain should be recognized in profit or loss when the asset is derecognized (IAS 16.68). Derecognition occurs when the asset is disposed of or when no future economic benefits are expected from its use or disposal (IAS 16.67).\\n\\n4. **Presentation in Financial Statements:**\\n   - Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\\n\\n### Example Journal Entry:\\nAssume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\\n\\n- **Journal Entry:**\\n  - Debit: Cash/Bank $70,000\\n  - Credit: Fixed Asset $50,000\\n  - Credit: Gain on Sale of Fixed Asset $20,000\\n\\n### Relevant IFRS/IAS Paragraphs:\\n- **IAS 16.6:** Definition of carrying amount.\\n- **IAS 16.67:** Derecognition of an asset.\\n- **IAS 16.68:** Recognition of gain or loss on derecognition.\\n- **IAS 16.71:** Calculation of gain or loss on disposal.\\n- **IAS 1.97:** Presentation of gains in the income statement.\\n\\n### Sources:\\n- IAS 16 \"Property, Plant and Equipment\"\\n- IAS 1 \"Presentation of Financial Statements\"\\n\\nBy following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.', 'metadata': []}, 'unified_response': {'answer': 'To account for gains on the sale of fixed assets, follow the guidance provided by IAS 16 \"Property, Plant, and Equipment.\"\\n\\n### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\\n\\n1. **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (IAS 16.67-72).\\n2. **Calculate the Gain**: The gain is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (IAS 16.71).\\n3. **Recognition of Gain**: Any gain arising from the derecognition of the asset should be recognized in profit or loss (IAS 16.68).\\n4. **Presentation in Financial Statements**: Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\\n\\n### Example Journal Entry:\\nAssume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\\n\\n- **Journal Entry:**\\n  - Debit: Cash/Bank $70,000\\n  - Credit: Fixed Asset $50,000\\n  - Credit: Gain on Sale of Fixed Asset $20,000\\n\\n### Relevant IFRS/IAS Paragraphs:\\n- **IAS 16.6**: Definition of carrying amount.\\n- **IAS 16.67**: Derecognition of an asset.\\n- **IAS 16.68**: Recognition of gain or loss on derecognition.\\n- **IAS 16.71**: Calculation of gain or loss on disposal.\\n- **IAS 1.97**: Presentation of gains in the income statement.\\n\\nBy following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.', 'metadata': []}, 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: OVERALL STATUS CHECK NODE------\n",
            "-------------------------------- \u001b[1;31mFinal Answer\u001b[0m --------------------------------\n"
          ]
        },
        {
          "data": {
            "text/markdown": [
              "**FINAL ANSWER:** <font color=\"red\">### IFRS: \n",
              "As per IAS 16, gains on the sale of fixed assets (property, plant, and equipment) should be accounted for as follows:\n",
              "\n",
              "- **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (paragraph 67-72).\n",
              "- **Recognition of Gain or Loss**: Any gain or loss arising from the derecognition of the asset should be recognized in profit or loss. This gain or loss is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (paragraph 71).\n",
              "\n",
              "Therefore, the gain on the sale of fixed assets should be recognized in the profit or loss statement at the date of derecognition.\n",
              "\n",
              "---\n",
              "\n",
              "### Annual Reports: \n",
              "NO GUIDANCE\n",
              "\n",
              "---\n",
              "\n",
              "### Foundational ChatGPT: \n",
              "To account for gains on the sale of fixed assets, you need to follow the guidance provided by IAS 16 \"Property, Plant and Equipment\" and IFRS 5 \"Non-current Assets Held for Sale and Discontinued Operations\" if applicable.\n",
              "\n",
              "### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\n",
              "\n",
              "1. **Determine the Carrying Amount:**\n",
              "   - The carrying amount of the fixed asset is its cost less any accumulated depreciation and any accumulated impairment losses (IAS 16.6).\n",
              "\n",
              "2. **Calculate the Gain:**\n",
              "   - The gain on the sale of a fixed asset is calculated as the difference between the net disposal proceeds and the carrying amount of the asset at the time of sale (IAS 16.71).\n",
              "\n",
              "3. **Recognize the Gain:**\n",
              "   - The gain should be recognized in profit or loss when the asset is derecognized (IAS 16.68). Derecognition occurs when the asset is disposed of or when no future economic benefits are expected from its use or disposal (IAS 16.67).\n",
              "\n",
              "4. **Presentation in Financial Statements:**\n",
              "   - Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\n",
              "\n",
              "### Example Journal Entry:\n",
              "Assume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\n",
              "\n",
              "- **Journal Entry:**\n",
              "  - Debit: Cash/Bank $70,000\n",
              "  - Credit: Fixed Asset $50,000\n",
              "  - Credit: Gain on Sale of Fixed Asset $20,000\n",
              "\n",
              "### Relevant IFRS/IAS Paragraphs:\n",
              "- **IAS 16.6:** Definition of carrying amount.\n",
              "- **IAS 16.67:** Derecognition of an asset.\n",
              "- **IAS 16.68:** Recognition of gain or loss on derecognition.\n",
              "- **IAS 16.71:** Calculation of gain or loss on disposal.\n",
              "- **IAS 1.97:** Presentation of gains in the income statement.\n",
              "\n",
              "### Sources:\n",
              "- IAS 16 \"Property, Plant and Equipment\"\n",
              "- IAS 1 \"Presentation of Financial Statements\"\n",
              "\n",
              "By following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.\n",
              "\n",
              "---\n",
              "\n",
              "### Unified Response\n",
              "To account for gains on the sale of fixed assets, follow the guidance provided by IAS 16 \"Property, Plant, and Equipment.\"\n",
              "\n",
              "### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\n",
              "\n",
              "1. **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (IAS 16.67-72).\n",
              "2. **Calculate the Gain**: The gain is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (IAS 16.71).\n",
              "3. **Recognition of Gain**: Any gain arising from the derecognition of the asset should be recognized in profit or loss (IAS 16.68).\n",
              "4. **Presentation in Financial Statements**: Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\n",
              "\n",
              "### Example Journal Entry:\n",
              "Assume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\n",
              "\n",
              "- **Journal Entry:**\n",
              "  - Debit: Cash/Bank $70,000\n",
              "  - Credit: Fixed Asset $50,000\n",
              "  - Credit: Gain on Sale of Fixed Asset $20,000\n",
              "\n",
              "### Relevant IFRS/IAS Paragraphs:\n",
              "- **IAS 16.6**: Definition of carrying amount.\n",
              "- **IAS 16.67**: Derecognition of an asset.\n",
              "- **IAS 16.68**: Recognition of gain or loss on derecognition.\n",
              "- **IAS 16.71**: Calculation of gain or loss on disposal.\n",
              "- **IAS 1.97**: Presentation of gains in the income statement.\n",
              "\n",
              "By following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.\n",
              "\n",
              "</font>"
            ],
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'How do I account for Gains on sales of fixed assets?', 'topic': 'DUMMY TOPIC', 'final_answer': '### IFRS: \\nAs per IAS 16, gains on the sale of fixed assets (property, plant, and equipment) should be accounted for as follows:\\n\\n- **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (paragraph 67-72).\\n- **Recognition of Gain or Loss**: Any gain or loss arising from the derecognition of the asset should be recognized in profit or loss. This gain or loss is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (paragraph 71).\\n\\nTherefore, the gain on the sale of fixed assets should be recognized in the profit or loss statement at the date of derecognition.\\n\\n---\\n\\n### Annual Reports: \\nNO GUIDANCE\\n\\n---\\n\\n### Foundational ChatGPT: \\nTo account for gains on the sale of fixed assets, you need to follow the guidance provided by IAS 16 \"Property, Plant and Equipment\" and IFRS 5 \"Non-current Assets Held for Sale and Discontinued Operations\" if applicable.\\n\\n### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\\n\\n1. **Determine the Carrying Amount:**\\n   - The carrying amount of the fixed asset is its cost less any accumulated depreciation and any accumulated impairment losses (IAS 16.6).\\n\\n2. **Calculate the Gain:**\\n   - The gain on the sale of a fixed asset is calculated as the difference between the net disposal proceeds and the carrying amount of the asset at the time of sale (IAS 16.71).\\n\\n3. **Recognize the Gain:**\\n   - The gain should be recognized in profit or loss when the asset is derecognized (IAS 16.68). Derecognition occurs when the asset is disposed of or when no future economic benefits are expected from its use or disposal (IAS 16.67).\\n\\n4. **Presentation in Financial Statements:**\\n   - Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\\n\\n### Example Journal Entry:\\nAssume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\\n\\n- **Journal Entry:**\\n  - Debit: Cash/Bank $70,000\\n  - Credit: Fixed Asset $50,000\\n  - Credit: Gain on Sale of Fixed Asset $20,000\\n\\n### Relevant IFRS/IAS Paragraphs:\\n- **IAS 16.6:** Definition of carrying amount.\\n- **IAS 16.67:** Derecognition of an asset.\\n- **IAS 16.68:** Recognition of gain or loss on derecognition.\\n- **IAS 16.71:** Calculation of gain or loss on disposal.\\n- **IAS 1.97:** Presentation of gains in the income statement.\\n\\n### Sources:\\n- IAS 16 \"Property, Plant and Equipment\"\\n- IAS 1 \"Presentation of Financial Statements\"\\n\\nBy following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.\\n\\n---\\n\\n### Unified Response\\nTo account for gains on the sale of fixed assets, follow the guidance provided by IAS 16 \"Property, Plant, and Equipment.\"\\n\\n### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\\n\\n1. **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (IAS 16.67-72).\\n2. **Calculate the Gain**: The gain is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (IAS 16.71).\\n3. **Recognition of Gain**: Any gain arising from the derecognition of the asset should be recognized in profit or loss (IAS 16.68).\\n4. **Presentation in Financial Statements**: Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\\n\\n### Example Journal Entry:\\nAssume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\\n\\n- **Journal Entry:**\\n  - Debit: Cash/Bank $70,000\\n  - Credit: Fixed Asset $50,000\\n  - Credit: Gain on Sale of Fixed Asset $20,000\\n\\n### Relevant IFRS/IAS Paragraphs:\\n- **IAS 16.6**: Definition of carrying amount.\\n- **IAS 16.67**: Derecognition of an asset.\\n- **IAS 16.68**: Recognition of gain or loss on derecognition.\\n- **IAS 16.71**: Calculation of gain or loss on disposal.\\n- **IAS 1.97**: Presentation of gains in the income statement.\\n\\nBy following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.\\n\\n', 'finance_check': {'observation': 'Yes'}, 'query_rerouter_check': {'observation': 'FRA'}, 'source_detector_check': {'observation': ['annual_reports_answer_node', 'fm_answer_node', 'ifrs_answer_node']}, 'overall_status_check': {'observation': 'Completed'}, 'ifrs_response': {'answer': 'As per IAS 16, gains on the sale of fixed assets (property, plant, and equipment) should be accounted for as follows:\\n\\n- **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (paragraph 67-72).\\n- **Recognition of Gain or Loss**: Any gain or loss arising from the derecognition of the asset should be recognized in profit or loss. This gain or loss is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (paragraph 71).\\n\\nTherefore, the gain on the sale of fixed assets should be recognized in the profit or loss statement at the date of derecognition.', 'metadata': []}, 'annual_reports_response': {'answer': 'NO GUIDANCE', 'metadata': []}, 'fm_response': {'answer': 'To account for gains on the sale of fixed assets, you need to follow the guidance provided by IAS 16 \"Property, Plant and Equipment\" and IFRS 5 \"Non-current Assets Held for Sale and Discontinued Operations\" if applicable.\\n\\n### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\\n\\n1. **Determine the Carrying Amount:**\\n   - The carrying amount of the fixed asset is its cost less any accumulated depreciation and any accumulated impairment losses (IAS 16.6).\\n\\n2. **Calculate the Gain:**\\n   - The gain on the sale of a fixed asset is calculated as the difference between the net disposal proceeds and the carrying amount of the asset at the time of sale (IAS 16.71).\\n\\n3. **Recognize the Gain:**\\n   - The gain should be recognized in profit or loss when the asset is derecognized (IAS 16.68). Derecognition occurs when the asset is disposed of or when no future economic benefits are expected from its use or disposal (IAS 16.67).\\n\\n4. **Presentation in Financial Statements:**\\n   - Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\\n\\n### Example Journal Entry:\\nAssume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\\n\\n- **Journal Entry:**\\n  - Debit: Cash/Bank $70,000\\n  - Credit: Fixed Asset $50,000\\n  - Credit: Gain on Sale of Fixed Asset $20,000\\n\\n### Relevant IFRS/IAS Paragraphs:\\n- **IAS 16.6:** Definition of carrying amount.\\n- **IAS 16.67:** Derecognition of an asset.\\n- **IAS 16.68:** Recognition of gain or loss on derecognition.\\n- **IAS 16.71:** Calculation of gain or loss on disposal.\\n- **IAS 1.97:** Presentation of gains in the income statement.\\n\\n### Sources:\\n- IAS 16 \"Property, Plant and Equipment\"\\n- IAS 1 \"Presentation of Financial Statements\"\\n\\nBy following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.', 'metadata': []}, 'unified_response': {'answer': 'To account for gains on the sale of fixed assets, follow the guidance provided by IAS 16 \"Property, Plant, and Equipment.\"\\n\\n### Step-by-Step Accounting for Gains on Sales of Fixed Assets:\\n\\n1. **Derecognition**: The carrying amount of the asset should be derecognized at the date of disposal (IAS 16.67-72).\\n2. **Calculate the Gain**: The gain is calculated as the difference between the net disposal proceeds and the carrying amount of the asset (IAS 16.71).\\n3. **Recognition of Gain**: Any gain arising from the derecognition of the asset should be recognized in profit or loss (IAS 16.68).\\n4. **Presentation in Financial Statements**: Gains on the sale of fixed assets should be presented in the income statement as part of other income or separately if material (IAS 1.97).\\n\\n### Example Journal Entry:\\nAssume a fixed asset with a carrying amount of $50,000 is sold for $70,000.\\n\\n- **Journal Entry:**\\n  - Debit: Cash/Bank $70,000\\n  - Credit: Fixed Asset $50,000\\n  - Credit: Gain on Sale of Fixed Asset $20,000\\n\\n### Relevant IFRS/IAS Paragraphs:\\n- **IAS 16.6**: Definition of carrying amount.\\n- **IAS 16.67**: Derecognition of an asset.\\n- **IAS 16.68**: Recognition of gain or loss on derecognition.\\n- **IAS 16.71**: Calculation of gain or loss on disposal.\\n- **IAS 1.97**: Presentation of gains in the income statement.\\n\\nBy following these steps and referencing the relevant IFRS/IAS paragraphs, you can accurately account for gains on the sale of fixed assets in compliance with international financial reporting standards.', 'metadata': []}, 'intermediate_steps': []}\u001b[0m\n",
            "--------------------------------------------------------\n",
            "\u001b[1;31mTotal Time Taken - [24.6]\u001b[0m\n",
            "--------------------------------------------------------\n"
          ]
        }
      ],
      "source": [
        "question = \"How do I account for Gains on sales of fixed assets?\"\n",
        "run_answer(question, 89)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1321e926-33d7-4d59-bf51-84c67411a440",
      "metadata": {
        "tags": [],
        "id": "1321e926-33d7-4d59-bf51-84c67411a440",
        "outputId": "09a7889a-5d10-4c74-993b-70cc2f68e108"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'Where do i find company master data change request form?', 'final_answer': '', 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: TOPIC MODELLING NODE------\n",
            "============================================\n",
            "{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'Where do i find company master data change request form?', 'topic': None, 'requested_datasources': None, 'final_answer': '', 'finance_check': None, 'query_rerouter_check': None, 'source_detector_check': None, 'overall_status_check': None, 'generic_response': None, 'web_response': None, 'ifrs_response': None, 'annual_reports_response': None, 'fm_response': None, 'unified_response': None, 'intermediate_steps': []}\n",
            "============================================\n",
            "------OBSERVATION: DUMMY TOPIC------\n",
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'Where do i find company master data change request form?', 'topic': 'DUMMY TOPIC', 'final_answer': '', 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: FINANCE CHECK NODE------\n",
            "------OBSERVATION: Yes------\n",
            "------DECISION: INVOKE QUERY REROUTER NODE------\n",
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'Where do i find company master data change request form?', 'topic': 'DUMMY TOPIC', 'final_answer': '', 'finance_check': {'observation': 'Yes'}, 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: QUERY REROUTER NODE------\n",
            "------OBSERVATION: FRA------\n",
            "------DECISION: INVOKE SOURCE DETECTOR NODE------\n",
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'Where do i find company master data change request form?', 'topic': 'DUMMY TOPIC', 'final_answer': '', 'finance_check': {'observation': 'Yes'}, 'query_rerouter_check': {'observation': 'FRA'}, 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: SOURCE DETECTOR NODE------\n",
            "------SOURCES DETECTED: ['annual_reports_answer_node', 'fm_answer_node', 'ifrs_answer_node']------\n",
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'Where do i find company master data change request form?', 'topic': 'DUMMY TOPIC', 'final_answer': '', 'finance_check': {'observation': 'Yes'}, 'query_rerouter_check': {'observation': 'FRA'}, 'source_detector_check': {'observation': ['annual_reports_answer_node', 'fm_answer_node', 'ifrs_answer_node']}, 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: IFRS ANSWER NODE------\n",
            "------ENTERING: ANNUAL REPORTS ANSWER NODE------\n",
            "------ENTERING: FOUNDATIONAL ANSWER NODE------\n"
          ]
        },
        {
          "data": {
            "text/markdown": [
              "**IFRS ANSWER:** <font color=\"red\">NO GUIDANCE</font>"
            ],
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/markdown": [
              "**ANNUAL REPORTS ANSWER:** <font color=\"red\">You can find the company master data change request form on the Novartis Supplier Portal. Here is the link to access it: [Novartis Supplier Portal](https://www.novartis.com/supplier-portal).</font>"
            ],
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "text/markdown": [
              "**FOUNDATIONAL ANSWER:** <font color=\"red\">To find the company master data change request form at Novartis, you should typically refer to the internal resources provided by the company's finance or IT departments. This form is usually part of the internal control processes and is used to ensure that any changes to the master data are properly documented and authorized.\n",
              "\n",
              "Here are the steps you can follow to locate the form:\n",
              "\n",
              "1. **Intranet or Internal Portal**: Check the Novartis intranet or internal employee portal. These platforms often have sections dedicated to forms and templates, including those for financial and administrative purposes.\n",
              "\n",
              "2. **Finance Department**: Contact the finance department directly. They can provide you with the necessary forms and guide you through the process of submitting a change request.\n",
              "\n",
              "3. **IT Support**: Sometimes, the IT department manages the master data systems. They can also provide the form or direct you to the appropriate resource.\n",
              "\n",
              "4. **Internal Policies and Procedures Manual**: Refer to the internal policies and procedures manual, which may include instructions on how to request changes to company master data and where to find the relevant forms.\n",
              "\n",
              "5. **SAP or ERP System**: If Novartis uses an ERP system like SAP, the form might be available within the system itself. You can check the help section or contact the system administrator for assistance.\n",
              "\n",
              "Since this is an internal document, it is not governed by IFRS or IAS standards, and there are no specific paragraphs from these standards that apply to the location of the form. However, maintaining accurate and up-to-date master data is crucial for financial reporting and compliance with standards such as IFRS 7 (Financial Instruments: Disclosures) and IFRS 9 (Financial Instruments), which require accurate data for proper financial disclosures.\n",
              "\n",
              "For further assistance, you may refer to internal communication channels or consult with your supervisor or manager.</font>"
            ],
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'Where do i find company master data change request form?', 'topic': 'DUMMY TOPIC', 'final_answer': '', 'finance_check': {'observation': 'Yes'}, 'query_rerouter_check': {'observation': 'FRA'}, 'source_detector_check': {'observation': ['annual_reports_answer_node', 'fm_answer_node', 'ifrs_answer_node']}, 'ifrs_response': {'answer': 'NO GUIDANCE', 'metadata': []}, 'annual_reports_response': {'answer': 'You can find the company master data change request form on the Novartis Supplier Portal. Here is the link to access it: [Novartis Supplier Portal](https://www.novartis.com/supplier-portal).', 'metadata': []}, 'fm_response': {'answer': \"To find the company master data change request form at Novartis, you should typically refer to the internal resources provided by the company's finance or IT departments. This form is usually part of the internal control processes and is used to ensure that any changes to the master data are properly documented and authorized.\\n\\nHere are the steps you can follow to locate the form:\\n\\n1. **Intranet or Internal Portal**: Check the Novartis intranet or internal employee portal. These platforms often have sections dedicated to forms and templates, including those for financial and administrative purposes.\\n\\n2. **Finance Department**: Contact the finance department directly. They can provide you with the necessary forms and guide you through the process of submitting a change request.\\n\\n3. **IT Support**: Sometimes, the IT department manages the master data systems. They can also provide the form or direct you to the appropriate resource.\\n\\n4. **Internal Policies and Procedures Manual**: Refer to the internal policies and procedures manual, which may include instructions on how to request changes to company master data and where to find the relevant forms.\\n\\n5. **SAP or ERP System**: If Novartis uses an ERP system like SAP, the form might be available within the system itself. You can check the help section or contact the system administrator for assistance.\\n\\nSince this is an internal document, it is not governed by IFRS or IAS standards, and there are no specific paragraphs from these standards that apply to the location of the form. However, maintaining accurate and up-to-date master data is crucial for financial reporting and compliance with standards such as IFRS 7 (Financial Instruments: Disclosures) and IFRS 9 (Financial Instruments), which require accurate data for proper financial disclosures.\\n\\nFor further assistance, you may refer to internal communication channels or consult with your supervisor or manager.\", 'metadata': []}, 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: UNIFIED ANSWER NODE------\n"
          ]
        },
        {
          "data": {
            "application/json": {
              "annual_reports_response": {
                "answer": "You can find the company master data change request form on the Novartis Supplier Portal. Here is the link to access it: [Novartis Supplier Portal](https://www.novartis.com/supplier-portal).",
                "metadata": []
              },
              "final_answer": "",
              "finance_check": {
                "observation": "Yes"
              },
              "fm_response": {
                "answer": "To find the company master data change request form at Novartis, you should typically refer to the internal resources provided by the company's finance or IT departments. This form is usually part of the internal control processes and is used to ensure that any changes to the master data are properly documented and authorized.\n\nHere are the steps you can follow to locate the form:\n\n1. **Intranet or Internal Portal**: Check the Novartis intranet or internal employee portal. These platforms often have sections dedicated to forms and templates, including those for financial and administrative purposes.\n\n2. **Finance Department**: Contact the finance department directly. They can provide you with the necessary forms and guide you through the process of submitting a change request.\n\n3. **IT Support**: Sometimes, the IT department manages the master data systems. They can also provide the form or direct you to the appropriate resource.\n\n4. **Internal Policies and Procedures Manual**: Refer to the internal policies and procedures manual, which may include instructions on how to request changes to company master data and where to find the relevant forms.\n\n5. **SAP or ERP System**: If Novartis uses an ERP system like SAP, the form might be available within the system itself. You can check the help section or contact the system administrator for assistance.\n\nSince this is an internal document, it is not governed by IFRS or IAS standards, and there are no specific paragraphs from these standards that apply to the location of the form. However, maintaining accurate and up-to-date master data is crucial for financial reporting and compliance with standards such as IFRS 7 (Financial Instruments: Disclosures) and IFRS 9 (Financial Instruments), which require accurate data for proper financial disclosures.\n\nFor further assistance, you may refer to internal communication channels or consult with your supervisor or manager.",
                "metadata": []
              },
              "generic_response": null,
              "ifrs_response": {
                "answer": "NO GUIDANCE",
                "metadata": []
              },
              "intermediate_steps": [],
              "operation_id": 123456,
              "overall_status_check": null,
              "query_rerouter_check": {
                "observation": "FRA"
              },
              "question": "Where do i find company master data change request form?",
              "requested_datasources": null,
              "source_detector_check": {
                "observation": [
                  "annual_reports_answer_node",
                  "fm_answer_node",
                  "ifrs_answer_node"
                ]
              },
              "topic": "DUMMY TOPIC",
              "unified_response": null,
              "user_id": "nalabsr1",
              "web_response": null
            },
            "text/plain": [
              "<IPython.core.display.JSON object>"
            ]
          },
          "metadata": {
            "application/json": {
              "expanded": false,
              "root": "root"
            }
          },
          "output_type": "display_data"
        },
        {
          "data": {
            "text/markdown": [
              "**UNIFIED ANSWER:** <font color=\"red\">To find the company master data change request form at Novartis, you can access it on the [Novartis Supplier Portal](https://www.novartis.com/supplier-portal). This form is part of the internal control processes to ensure that any changes to the master data are properly documented and authorized. For further assistance, you may refer to internal communication channels or consult with your supervisor or manager.</font>"
            ],
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'Where do i find company master data change request form?', 'topic': 'DUMMY TOPIC', 'final_answer': \"### IFRS: \\nNO GUIDANCE\\n\\n---\\n\\n### Annual Reports: \\nYou can find the company master data change request form on the Novartis Supplier Portal. Here is the link to access it: [Novartis Supplier Portal](https://www.novartis.com/supplier-portal).\\n\\n---\\n\\n### Foundational ChatGPT: \\nTo find the company master data change request form at Novartis, you should typically refer to the internal resources provided by the company's finance or IT departments. This form is usually part of the internal control processes and is used to ensure that any changes to the master data are properly documented and authorized.\\n\\nHere are the steps you can follow to locate the form:\\n\\n1. **Intranet or Internal Portal**: Check the Novartis intranet or internal employee portal. These platforms often have sections dedicated to forms and templates, including those for financial and administrative purposes.\\n\\n2. **Finance Department**: Contact the finance department directly. They can provide you with the necessary forms and guide you through the process of submitting a change request.\\n\\n3. **IT Support**: Sometimes, the IT department manages the master data systems. They can also provide the form or direct you to the appropriate resource.\\n\\n4. **Internal Policies and Procedures Manual**: Refer to the internal policies and procedures manual, which may include instructions on how to request changes to company master data and where to find the relevant forms.\\n\\n5. **SAP or ERP System**: If Novartis uses an ERP system like SAP, the form might be available within the system itself. You can check the help section or contact the system administrator for assistance.\\n\\nSince this is an internal document, it is not governed by IFRS or IAS standards, and there are no specific paragraphs from these standards that apply to the location of the form. However, maintaining accurate and up-to-date master data is crucial for financial reporting and compliance with standards such as IFRS 7 (Financial Instruments: Disclosures) and IFRS 9 (Financial Instruments), which require accurate data for proper financial disclosures.\\n\\nFor further assistance, you may refer to internal communication channels or consult with your supervisor or manager.\\n\\n---\\n\\n### Unified Response\\nTo find the company master data change request form at Novartis, you can access it on the [Novartis Supplier Portal](https://www.novartis.com/supplier-portal). This form is part of the internal control processes to ensure that any changes to the master data are properly documented and authorized. For further assistance, you may refer to internal communication channels or consult with your supervisor or manager.\\n\\n\", 'finance_check': {'observation': 'Yes'}, 'query_rerouter_check': {'observation': 'FRA'}, 'source_detector_check': {'observation': ['annual_reports_answer_node', 'fm_answer_node', 'ifrs_answer_node']}, 'ifrs_response': {'answer': 'NO GUIDANCE', 'metadata': []}, 'annual_reports_response': {'answer': 'You can find the company master data change request form on the Novartis Supplier Portal. Here is the link to access it: [Novartis Supplier Portal](https://www.novartis.com/supplier-portal).', 'metadata': []}, 'fm_response': {'answer': \"To find the company master data change request form at Novartis, you should typically refer to the internal resources provided by the company's finance or IT departments. This form is usually part of the internal control processes and is used to ensure that any changes to the master data are properly documented and authorized.\\n\\nHere are the steps you can follow to locate the form:\\n\\n1. **Intranet or Internal Portal**: Check the Novartis intranet or internal employee portal. These platforms often have sections dedicated to forms and templates, including those for financial and administrative purposes.\\n\\n2. **Finance Department**: Contact the finance department directly. They can provide you with the necessary forms and guide you through the process of submitting a change request.\\n\\n3. **IT Support**: Sometimes, the IT department manages the master data systems. They can also provide the form or direct you to the appropriate resource.\\n\\n4. **Internal Policies and Procedures Manual**: Refer to the internal policies and procedures manual, which may include instructions on how to request changes to company master data and where to find the relevant forms.\\n\\n5. **SAP or ERP System**: If Novartis uses an ERP system like SAP, the form might be available within the system itself. You can check the help section or contact the system administrator for assistance.\\n\\nSince this is an internal document, it is not governed by IFRS or IAS standards, and there are no specific paragraphs from these standards that apply to the location of the form. However, maintaining accurate and up-to-date master data is crucial for financial reporting and compliance with standards such as IFRS 7 (Financial Instruments: Disclosures) and IFRS 9 (Financial Instruments), which require accurate data for proper financial disclosures.\\n\\nFor further assistance, you may refer to internal communication channels or consult with your supervisor or manager.\", 'metadata': []}, 'unified_response': {'answer': 'To find the company master data change request form at Novartis, you can access it on the [Novartis Supplier Portal](https://www.novartis.com/supplier-portal). This form is part of the internal control processes to ensure that any changes to the master data are properly documented and authorized. For further assistance, you may refer to internal communication channels or consult with your supervisor or manager.', 'metadata': []}, 'intermediate_steps': []}\u001b[0m\n",
            "------ENTERING: OVERALL STATUS CHECK NODE------\n",
            "-------------------------------- \u001b[1;31mFinal Answer\u001b[0m --------------------------------\n"
          ]
        },
        {
          "data": {
            "text/markdown": [
              "**FINAL ANSWER:** <font color=\"red\">### IFRS: \n",
              "NO GUIDANCE\n",
              "\n",
              "---\n",
              "\n",
              "### Annual Reports: \n",
              "You can find the company master data change request form on the Novartis Supplier Portal. Here is the link to access it: [Novartis Supplier Portal](https://www.novartis.com/supplier-portal).\n",
              "\n",
              "---\n",
              "\n",
              "### Foundational ChatGPT: \n",
              "To find the company master data change request form at Novartis, you should typically refer to the internal resources provided by the company's finance or IT departments. This form is usually part of the internal control processes and is used to ensure that any changes to the master data are properly documented and authorized.\n",
              "\n",
              "Here are the steps you can follow to locate the form:\n",
              "\n",
              "1. **Intranet or Internal Portal**: Check the Novartis intranet or internal employee portal. These platforms often have sections dedicated to forms and templates, including those for financial and administrative purposes.\n",
              "\n",
              "2. **Finance Department**: Contact the finance department directly. They can provide you with the necessary forms and guide you through the process of submitting a change request.\n",
              "\n",
              "3. **IT Support**: Sometimes, the IT department manages the master data systems. They can also provide the form or direct you to the appropriate resource.\n",
              "\n",
              "4. **Internal Policies and Procedures Manual**: Refer to the internal policies and procedures manual, which may include instructions on how to request changes to company master data and where to find the relevant forms.\n",
              "\n",
              "5. **SAP or ERP System**: If Novartis uses an ERP system like SAP, the form might be available within the system itself. You can check the help section or contact the system administrator for assistance.\n",
              "\n",
              "Since this is an internal document, it is not governed by IFRS or IAS standards, and there are no specific paragraphs from these standards that apply to the location of the form. However, maintaining accurate and up-to-date master data is crucial for financial reporting and compliance with standards such as IFRS 7 (Financial Instruments: Disclosures) and IFRS 9 (Financial Instruments), which require accurate data for proper financial disclosures.\n",
              "\n",
              "For further assistance, you may refer to internal communication channels or consult with your supervisor or manager.\n",
              "\n",
              "---\n",
              "\n",
              "### Unified Response\n",
              "To find the company master data change request form at Novartis, you can access it on the [Novartis Supplier Portal](https://www.novartis.com/supplier-portal). This form is part of the internal control processes to ensure that any changes to the master data are properly documented and authorized. For further assistance, you may refer to internal communication channels or consult with your supervisor or manager.\n",
              "\n",
              "</font>"
            ],
            "text/plain": [
              "<IPython.core.display.Markdown object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\u001b[1;34m{'operation_id': 123456, 'user_id': 'nalabsr1', 'question': 'Where do i find company master data change request form?', 'topic': 'DUMMY TOPIC', 'final_answer': \"### IFRS: \\nNO GUIDANCE\\n\\n---\\n\\n### Annual Reports: \\nYou can find the company master data change request form on the Novartis Supplier Portal. Here is the link to access it: [Novartis Supplier Portal](https://www.novartis.com/supplier-portal).\\n\\n---\\n\\n### Foundational ChatGPT: \\nTo find the company master data change request form at Novartis, you should typically refer to the internal resources provided by the company's finance or IT departments. This form is usually part of the internal control processes and is used to ensure that any changes to the master data are properly documented and authorized.\\n\\nHere are the steps you can follow to locate the form:\\n\\n1. **Intranet or Internal Portal**: Check the Novartis intranet or internal employee portal. These platforms often have sections dedicated to forms and templates, including those for financial and administrative purposes.\\n\\n2. **Finance Department**: Contact the finance department directly. They can provide you with the necessary forms and guide you through the process of submitting a change request.\\n\\n3. **IT Support**: Sometimes, the IT department manages the master data systems. They can also provide the form or direct you to the appropriate resource.\\n\\n4. **Internal Policies and Procedures Manual**: Refer to the internal policies and procedures manual, which may include instructions on how to request changes to company master data and where to find the relevant forms.\\n\\n5. **SAP or ERP System**: If Novartis uses an ERP system like SAP, the form might be available within the system itself. You can check the help section or contact the system administrator for assistance.\\n\\nSince this is an internal document, it is not governed by IFRS or IAS standards, and there are no specific paragraphs from these standards that apply to the location of the form. However, maintaining accurate and up-to-date master data is crucial for financial reporting and compliance with standards such as IFRS 7 (Financial Instruments: Disclosures) and IFRS 9 (Financial Instruments), which require accurate data for proper financial disclosures.\\n\\nFor further assistance, you may refer to internal communication channels or consult with your supervisor or manager.\\n\\n---\\n\\n### Unified Response\\nTo find the company master data change request form at Novartis, you can access it on the [Novartis Supplier Portal](https://www.novartis.com/supplier-portal). This form is part of the internal control processes to ensure that any changes to the master data are properly documented and authorized. For further assistance, you may refer to internal communication channels or consult with your supervisor or manager.\\n\\n\", 'finance_check': {'observation': 'Yes'}, 'query_rerouter_check': {'observation': 'FRA'}, 'source_detector_check': {'observation': ['annual_reports_answer_node', 'fm_answer_node', 'ifrs_answer_node']}, 'overall_status_check': {'observation': 'Completed'}, 'ifrs_response': {'answer': 'NO GUIDANCE', 'metadata': []}, 'annual_reports_response': {'answer': 'You can find the company master data change request form on the Novartis Supplier Portal. Here is the link to access it: [Novartis Supplier Portal](https://www.novartis.com/supplier-portal).', 'metadata': []}, 'fm_response': {'answer': \"To find the company master data change request form at Novartis, you should typically refer to the internal resources provided by the company's finance or IT departments. This form is usually part of the internal control processes and is used to ensure that any changes to the master data are properly documented and authorized.\\n\\nHere are the steps you can follow to locate the form:\\n\\n1. **Intranet or Internal Portal**: Check the Novartis intranet or internal employee portal. These platforms often have sections dedicated to forms and templates, including those for financial and administrative purposes.\\n\\n2. **Finance Department**: Contact the finance department directly. They can provide you with the necessary forms and guide you through the process of submitting a change request.\\n\\n3. **IT Support**: Sometimes, the IT department manages the master data systems. They can also provide the form or direct you to the appropriate resource.\\n\\n4. **Internal Policies and Procedures Manual**: Refer to the internal policies and procedures manual, which may include instructions on how to request changes to company master data and where to find the relevant forms.\\n\\n5. **SAP or ERP System**: If Novartis uses an ERP system like SAP, the form might be available within the system itself. You can check the help section or contact the system administrator for assistance.\\n\\nSince this is an internal document, it is not governed by IFRS or IAS standards, and there are no specific paragraphs from these standards that apply to the location of the form. However, maintaining accurate and up-to-date master data is crucial for financial reporting and compliance with standards such as IFRS 7 (Financial Instruments: Disclosures) and IFRS 9 (Financial Instruments), which require accurate data for proper financial disclosures.\\n\\nFor further assistance, you may refer to internal communication channels or consult with your supervisor or manager.\", 'metadata': []}, 'unified_response': {'answer': 'To find the company master data change request form at Novartis, you can access it on the [Novartis Supplier Portal](https://www.novartis.com/supplier-portal). This form is part of the internal control processes to ensure that any changes to the master data are properly documented and authorized. For further assistance, you may refer to internal communication channels or consult with your supervisor or manager.', 'metadata': []}, 'intermediate_steps': []}\u001b[0m\n",
            "--------------------------------------------------------\n",
            "\u001b[1;31mTotal Time Taken - [11.64]\u001b[0m\n",
            "--------------------------------------------------------\n"
          ]
        }
      ],
      "source": [
        "question = \"Where do i find company master data change request form?\"\n",
        "run_answer(question, 19)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1abb0d42-6578-4fa6-a890-319cc4dad264",
      "metadata": {
        "id": "1abb0d42-6578-4fa6-a890-319cc4dad264"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "0dfb77c9-3d6f-4ee2-90f0-65998f928dc8",
      "metadata": {
        "id": "0dfb77c9-3d6f-4ee2-90f0-65998f928dc8"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8ddce2de-0794-49bf-9cd3-fe6133e9fecc",
      "metadata": {
        "id": "8ddce2de-0794-49bf-9cd3-fe6133e9fecc"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}