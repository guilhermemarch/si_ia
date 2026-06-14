import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Configuracoes:
    nvidia_api_key: str
    nvidia_model: str
    nvidia_base_url: str
    max_tokens: int
    temperature: float
    top_p: float
    enable_thinking: bool
    port: int


def carregar_configuracoes() -> Configuracoes:
    return Configuracoes(
        nvidia_api_key=os.getenv("NVIDIA_API_KEY", ""),
        nvidia_model=os.getenv("NVIDIA_MODEL", "google/gemma-4-31b-it"),
        nvidia_base_url=os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1"),
        max_tokens=int(os.getenv("NVIDIA_MAX_TOKENS", "16384")),
        temperature=float(os.getenv("NVIDIA_TEMPERATURE", "1.00")),
        top_p=float(os.getenv("NVIDIA_TOP_P", "0.95")),
        enable_thinking=os.getenv("NVIDIA_ENABLE_THINKING", "true").lower() == "true",
        port=int(os.getenv("PORT", "8000")),
    )
