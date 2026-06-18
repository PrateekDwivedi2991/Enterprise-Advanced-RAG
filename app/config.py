from pydantic import BaseSettings, SettingsConfigDict
from qdrant_client import local
from sqlalchemy import false, true

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # === LLM & Embeddings ===
    OPENAI_API_KEY: str
    LLM_MODEL_ANSWER: str
    LLM_MODEL_GRADER: str
    EMBEDDING_MODEL: str

    QDRANT_URL: str
    QDRANT_API_KEY: str

    # === Database ===
    DATABASE_URL: str

    # === Cache (Upstash) ===
    UPSTASH_REDIS_REST_URL: str
    UPSTASH_REDIS_REST_TOKEN: str
    CACHE_TTL_EMBEDDINGS: int
    CACHE_TTL_RAG: int 
    CACHE_TTL_SQL_GEN: int
    CACHE_TTL_SQL_RESULT: int
    CACHE_TTL_INTENT: int

    STORAGE_BACKEND: str  # "local" or "s3"
    S3_CACHE_BUCKET: str  # Bucket name for caching (if using S3)
    AWS_REGION: str


    # === AWS S3 (for file uploads) ===
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    AWS_S3_BUCKET_NAME: str

    # === Web search ===
    TAVILY_API_KEY: str

    # === Auth ===
    JWT_SECRET: str
    JWT_EXPIRATION_MINUTES: int

    RATE_LIMIT_REQUESTS: int
    RATE_LIMIT_WINDOW_SECONDS: int
    MAX_TOKENS_PER_USER_DAILY: int
    AUTH_LOGIN_RATE_LIMIT_PER_MIN: int
    AUTH_REGISTER_RATE_LIMIT_PER_HOUR: int


    MAX_INPUT_TOKENS: int
    RESERVED_CONTEXT_TOKENS: int
    RESERVED_OUPUT_TOKENS: int

    # === Input restructuring ===


    # === Security thresholds ===
    PROMPT_TOXICITY_THRESHOLD: float
    OUTPUT_TOXICITY_THRESHOLD: float
    MAX_VALIDATION_RETRIES: int
    MAX_VALIDATION_RETRIES=2

    # === Retrieval defaults ===
    HYDE_NUM_HYPOTHESES: int
    HYDE_ENABLED_BY_DEFAULT: bool
    HYBRID_SEARCH_ENABLED: bool
    RRF_K: int
    RERANKER_BACKEND: str         # or "voyage"
    RERANKER_MODEL: str
    VOYAGE_API_KEY: str
    VOYAGE_MODEL: str
    RERANKER_INITIAL_TOP_K: int
    RERANKING_ENABLED_BY_DEFAULT: bool
    CRAG_RELEVANCE_THRESHOLD: float
    CRAG_AMBIGUOUS_THRESHOLD: float
    CRAG_ENABLED_BY_DEFAULT: bool
    REFLECTION_MIN_SCORE: float
    MAX_REFLECTION_RETRIES: int
    SELF_REFLECTIVE_ENABLED_BY_DEFAULT: bool

    # === Vanna ===
    VANNA_MODEL: str
    VANNA_TEMPERATURE: float
    VANNA_SEED: int

    LOG_JSON: bool                  # true in prod
    LOG_LEVEL: str = "INFO"

settings = Settings()