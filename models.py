from peewee import *
import config


db = PostgresqlDatabase(config.dbname, user=config.name)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class Boards(BaseModel):
    name = CharField()
    board_id = CharField(255)

    @classmethod  # converting obj to dict for the json
    def get_boards(cls):
        boards = cls.select(cls.name, cls.board_id)
        if boards != []:
            list_of_boards = []
            for i in boards:
                dict_of_boards = {}
                dict_of_boards['board_id'] = i.board_id
                dict_of_boards['name'] = i.name
                list_of_boards.append(dict_of_boards)
            return list_of_boards
        else:
            pass

    @classmethod
    def save_board(cls, board):
        cls.create(board_id=board['board_id'], name=board['name'])

    @classmethod
    def delete_boards(cls, board):
        board = cls.delete().where(board == cls.board_id)
        board.execute()



class Cards(BaseModel):
    board_id = CharField(255)
    name = CharField()
    status = CharField()
    card_id = CharField(255)

    @classmethod
    def get_cards(cls):
        cards = cls.select(cls.name, cls.board_id, cls.status, cls.card_id)
        if cards != []:
            list_of_cards = []
            for i in cards:
                dict_of_cards = {}
                dict_of_cards['board_id'] = i.board_id
                dict_of_cards['name'] = i.name
                dict_of_cards["status"] = i.status
                dict_of_cards["cardId"] = i.card_id
                list_of_cards.append(dict_of_cards)
            return list_of_cards
        else:
            pass

    @classmethod
    def save_card(cls, id, name, card_id):
        cls.create(board_id=id, name=name, status="nothing", card_id=card_id)

    @classmethod
    def update_card(cls, status, name):
        card = cls.update(status=status).where(name == cls.name)
        card.execute()

    @classmethod
    def delete_card(cls, card_id):
        print('itt bent vagyok')
        card = cls.delete().where(card_id == cls.card_id)
        card.execute()
