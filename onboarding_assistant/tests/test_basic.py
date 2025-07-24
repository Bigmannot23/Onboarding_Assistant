import os
import yaml

def test_knowledge_base_not_empty():
    """Ensure that the knowledge_base directory contains at least one Markdown file."""
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "knowledge_base")
    assert os.path.isdir(base_dir), "knowledge_base directory is missing"
    files = [f for f in os.listdir(base_dir) if f.endswith(".md")]
    assert files, "knowledge_base directory should contain at least one .md file"

def test_config_yaml_valid():
    """Ensure that config.yaml is valid YAML and contains required keys."""
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)))
    path = os.path.join(base_dir, "config.yaml")
    assert os.path.isfile(path), "config.yaml is missing"
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    for key in ["model", "temperature", "max_tokens", "top_k", "embed_model"]:
        assert key in config, f"Missing key {key} in config.yaml"