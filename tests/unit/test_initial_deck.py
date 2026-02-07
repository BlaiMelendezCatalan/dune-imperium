from dune_imperium.decks.initial import InitialDeck


def test_initial_deck_cards():

    initial_deck = InitialDeck().initialize()
    assert len(initial_deck.cards) == 10
    expected_cards = {
        "ConvincingArgument": 2,
        "Dagger": 2,
        "Diplomacy": 1,
        "DuneTheDesertPlanet": 2,
        "Reconnaissance": 1,
        "SignetRing": 1,
        "SeekAllies": 1,
    }
    generate_cards = {}
    for card in initial_deck.cards:
        if card.__class__.__name__ not in generate_cards:
            generate_cards[card.__class__.__name__] = 0
        generate_cards[card.__class__.__name__] += 1
    assert generate_cards == expected_cards



def test_initial_deck_cards_are_shuffled():

    initial_deck_1 = InitialDeck().initialize()
    initial_deck_2 = InitialDeck().initialize()
    assert initial_deck_1.cards != initial_deck_2.cards