from dataclasses import dataclass

@dataclass(frozen=True)
class DeploymentConfig:
    name: str
    image: str
    cpu: int
    memory: int
    replicas: int
    autoscaling: bool
    min_replicas: int | None
    max_replicas: int | None
    env: dict
    secrets: list


class DeploymentConfigBuilder:

    def __init__(self, name: str, image: str):
        self._name = name
        self._image = image
        self._cpu = 1
        self._memory = 1024
        self._replicas = 1
        self._autoscaling = False
        self._min_replicas = None
        self._max_replicas = None
        self._env = {}
        self._secrets = []

    def with_resources(self, cpu: int, memory: int):
        self._cpu = cpu
        self._memory = memory
        return self

    def with_replicas(self, replicas: int):
        self._replicas = replicas
        return self

    def enable_autoscaling(self, min_r: int, max_r: int):
        self._autoscaling = True
        self._min_replicas = min_r
        self._max_replicas = max_r
        return self

    def with_env(self, key: str, value: str):
        self._env[key] = value
        return self

    def with_secret(self, secret: str):
        self._secrets.append(secret)
        return self

    def build(self) -> DeploymentConfig:
        if self._autoscaling and self._replicas != 1:
            raise ValueError("Autoscaling and fixed replicas cannot be combined")

        return DeploymentConfig(
            name=self._name,
            image=self._image,
            cpu=self._cpu,
            memory=self._memory,
            replicas=self._replicas,
            autoscaling=self._autoscaling,
            min_replicas=self._min_replicas,
            max_replicas=self._max_replicas,
            env=self._env,
            secrets=self._secrets
        )


config = (
    DeploymentConfigBuilder("api-service", "api:1.2")
        .with_resources(cpu=2, memory=4096)
        .enable_autoscaling(min_r=2, max_r=10)
        .with_env("ENV", "prod")
        .with_secret("DB_PASSWORD")
        .build()
)

