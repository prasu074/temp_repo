from pydantic import Field, BaseSettings


class _Service(BaseSettings):
    HOST: str = Field(default="0.0.0.0", env="service_host")
    PORT: int = Field(default=9192, env="service_port")
    BUILD_DIR: str = Field(default="scripts/templates")
    PROXY: str = Field(default="gateway/plugin/<gen-proxy>")
    BACKEND_DIR: str = Field(default=".")


Service = _Service()
