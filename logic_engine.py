# logic_engine.py

class KnowledgeBase:
    """
    Declarative Knowledge Base storing facts and Horn Clause rules,
    with a data-driven Forward Chaining inference engine.
    """

    def __init__(self):
        # Attribute to store unique string facts
        self.facts = set()
        # Attribute to store rules as Tuples: (premise_list, conclusion_string)
        self.rules = []

    def tell_fact(self, fact_string: str):
        """Adds a fact to the facts set."""
        self.facts.add(fact_string)

    def tell_rule(self, premise_list: list, conclusion_string: str):
        """Appends a rule tuple (premises, conclusion) to the rules list."""
        self.rules.append((premise_list, conclusion_string))

    def clear_facts(self):
        """Clears all stored facts."""
        self.facts.clear()

    def forward_chain(self):
        """
        Data-Driven Forward Chaining algorithm using Modus Ponens.
        Iterates over rules until no new facts can be deduced.
        """
        new_facts_added = True
        while new_facts_added:
            new_facts_added = False
            for premises, conclusion in self.rules:
                if conclusion not in self.facts:
                    # Modus Ponens check: are all premises satisfied?
                    if all(p in self.facts for p in premises):
                        self.facts.add(conclusion)
                        new_facts_added = True