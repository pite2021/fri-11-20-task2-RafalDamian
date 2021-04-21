import multiprocessing
from dataclasses import dataclass, field


class Bank:

  def __init__(self, name, interest):
    self.name = name.title()
    self.interest = interest
    self.clients = []

  def welcome():
    return 'Welcome to our bank!'
  
  def add_client(self, client):
    client.bank = self.name
    self.clients.append(client.full_name())

  def delete_client(self, client):
    if self.check_client(client):
      client.bank = 'no bank'
      self.clients.remove(client.full_name())

  def change_bank(self, client, new_bank):
    if self.check_client(client):
      client.bank = new_bank.name
      self.delete_client(client)
      new_bank.add_client(client)

  def give_credit(self, client, ammount):
    if self.check_client(client):
      client.cash = ammount
      client.add_credit(self.name, self.interest, ammount)

  def transfer(self, client, target, ammount):
    if self.check_client(client):
      client.cash = - ammount
      target.cash = ammount
      
  def withdrawal(self, client, ammount):
    if self.check_client(client):
      client.cash = - ammount

  def deposit(self, client, ammount):
    if self.check_client(client):
      client.cash = - ammount
      client.add_deposit(self.name, self.interest, ammount)

  def check_client(self, client):
    return client.full_name() in self.clients


class Client:

  status = 'Client'

  def __init__(self, name, surname, cash=2000):
    self.name = name.title()
    self.surname = surname.title()
    self._cash = cash
    self.bank = 'no bank'
    self.credit_info = []
    self.deposits = []

  @property
  def cash(self):
    return self._cash

  @cash.getter
  def cash(self):
    return self._cash

  @cash.setter
  def cash(self, ammount):
    self._cash += ammount

  def add_credit(self, bank_name, interest, ammount):
    self.credit_info.append(
      {
      'bank' : bank_name,
      'ammount' : ammount,
      'interest' : interest
      }
    )

  def add_deposit(self, bank_name, interest, ammount):
    self.deposits.append(
      {
      'bank' : bank_name,
      'ammount' : ammount,
      'interest' : interest
      }
    )

  def full_name(self):
    return {'name':self.name, 'surname':self.surname}

  def client_info(self):
    return {
        'name' : self.name,
        'surname' : self.surname,
        'cash' : self.cash,
        'bank' : self.bank,
        'credits' : self.credit_info,
        'deposits' : self.deposits
        }

  def give_status(cls):
    return cls.status


class Admin(Client):
  status = 'Admin'


@dataclass
class UnderageClient:
  name : str
  surname : str
  cash : float
  bank : str = field(default='no bank')

  def full_name(self):
    return {'name':self.name, 'surname':self.surname}


if __name__ == '__main__':
  bank1 = Bank('alior', 0.02)
  bank2 = Bank('Pekao', 0.1)
  bank3 = Bank('mbank', 0.06)
  banks = [bank1, bank2, bank3]

  clients = []
  clients.append(Client('Maciek', 'Kazimierski', 5000))
  clients.append(Client('Pawel', 'Kopec', 2137))
  clients.append(Client ('Lukas', 'Holda', 6900))
  clients.append(Client('Bohdan', 'Pietrek', 25000))
  clients.append(Client('Adam', 'Pies', 5437))
  clients.append(Client ('Mikolaj', 'Nakladka', 690540))
  clients.append(Client('Witold', 'Gutowski', 5030))
  clients.append(Client('Anna', 'Koperek', 12137))
  clients.append(UnderageClient ('Ewelina', 'Kielbasa', 420))
  clients.append(UnderageClient('Krzysztof', 'Dziadowiec', 5021))
  clients.append(UnderageClient('Alina', 'Norek', 3456))
  clients.append(UnderageClient ('Juan', 'Sekundo', 54313))

  processes = []
  
  i = 0
  for j in range(4):
    for bank in banks:
      p = multiprocessing.Process(target = bank.add_client(clients[i]))
      p.start()
      processes.append(p)
      i = i+1

  for process in processes:
    process.join()

  for client in clients:
    print(client.bank)
  
  print(Admin.give_status(Admin))
  print(Client.give_status(Client))
  print(Bank.welcome())

  for i in range(0, 4):
    for bank in banks:
      if bank.check_client(clients[i]):
        print(clients[i].cash, clients[i+1].cash)
        bank.transfer(clients[i], clients[i+1], 200)
        print(clients[i].cash, clients[i+1].cash)

  for client in clients[4:8]:
    for bank in banks:
      if bank.check_client(client):
        print(client.cash)
        bank.withdrawal(client, 1000)
        print(client.cash)
        break

  for client in clients[8:]:
    if bank.check_client(client):
      bank1.change_bank(client, bank2)
      print(client.bank)

  for client in clients[0:6]:
    for bank in banks:
      if bank.check_client(client):
        bank.give_credit(client, 100000)
        print(client.client_info())
        break

  for client in clients[3:7]:
    for bank in banks:
      if bank.check_client(client):
        bank.deposit(client, 250)
        print(client.client_info())
        break


