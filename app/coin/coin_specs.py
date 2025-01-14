from dataclasses import dataclass
from decimal import Decimal

@dataclass
class CoinSpecs:
    algorithm: str 
    consensus_mechanism: str
    blockchain_network: str
    average_block_time: Decimal 
    security_features: str
    privacy_features: str
    max_supply: Decimal | None  
    genesis_block_date: str | None 
    token_type: str | None 
    governance_model: str | None   
    development_activity: str | None 
    hard_cap: Decimal | None  
    forking_coin: str | None 
    tokenomics: str | None

    def update_algorithm(self, new_algorithm: str):
        self.algorithm = new_algorithm

    def update_consensus_mechanism(self, new_consensus_mechanism: str):
        self.consensus_mechanism = new_consensus_mechanism

    def update_blockchain_network(self, new_blockchain_network: str):
        self.blockchain_network = new_blockchain_network

    def update_average_block_time(self, new_average_block_time: Decimal):
        self.average_block_time = new_average_block_time

    def update_security_features(self, new_security_features: str):
        self.security_features = new_security_features

    def update_privacy_features(self, new_privacy_features: str):
        self.privacy_features = new_privacy_features

    def update_max_supply(self, new_max_supply: Decimal):
        self.max_supply = new_max_supply

    def update_genesis_block_date(self, new_genesis_block_date: str):
        self.genesis_block_date = new_genesis_block_date

    def update_token_type(self, new_token_type: str):
        self.token_type = new_token_type

    def update_governance_model(self, new_governance_model: str):
        self.governance_model = new_governance_model

    def update_development_activity(self, new_development_activity: str):
        self.development_activity = new_development_activity

    def update_hard_cap(self, new_hard_cap: Decimal):
        self.hard_cap = new_hard_cap

    def update_forking_coin(self, new_forking_coin: str):
        self.forking_coin = new_forking_coin

    def update_tokenomics(self, new_tokenomics: str):
        self.tokenomics = new_tokenomics