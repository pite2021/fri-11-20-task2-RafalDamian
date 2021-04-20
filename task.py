

class Bank:

  def __init__(self, name, interest):
    self.name = name.title()
    self.interest = interest
    self.clients = []
  
  def add_client(self, client):
    client.bank = self.name
    self.clients.append(client.full_name())

  def delete_client(self, client):
    if client.full_name() in self.clients:
      client.bank = 'no bank'
      self.clients.remove(client.full_name())

  def change_bank(self, client, new_bank):
    if client.full_name() in self.clients:
      client.bank = new_bank.name
      self.delete_client(client)
      new_bank.add_client(client)

  def give_credit(self, client, ammount):
    if client.full_name() in self.clients:
      client.cash += ammount
      client.add_credit(self.name, self.interest, self.ammount)

  def transfer(self, client, target, ammount):
    if client.full_name() in self.clients:
      client.cash -= ammount
      target.cash += ammount
      
  def withdrawal(self, client, ammount):
    if client.full_name() in self.clients:
      client.cash -= ammount

  def deposit(self, client, ammount):
    if client.full_name() in self.clients:
      client.cash -= ammount
      client.add_credit(self.name, self.interest, self.ammount)



class Client:

  def __init__(self, name, surname, cash=2000):
    self.name = name.title()
    self.surname = surname.title()
    self.cash = cash
    self.bank = 'no bank'
    self.credit_info = []
    self.deposits = []

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


  
if __name__ == '__main__':
  alior = Bank('alior', 0.02)
  pekao = Bank('PEKAO', 0.1)
  wbk = Bank('WBK', 0.06)

  client1 = Client('Maciek', 'Kazimierczak', 5000)
  client2 = Client('Pawel', 'Kopec', 2137)
  client3 = Client ('Lukas', 'Cholda', 6900)
  client4 = Client('Bohdan', 'Pietrek', 25000)
  client5 = Client('Adam', 'Pies', 5437)
  client6 = Client ('Mikolaj', 'Nakladka', 690540)
  client7 = Client('Witold', 'Gutowski', 5030)
  client8 = Client('Anna', 'Koperek', 12137)
  client9 = Client ('Ewelina', 'Kielbasa', 420)
  client10 = Client('Krzysztof', 'Dziadowiec', 50900)
  client11 = Client('Alina', 'Norek', 3456)
  client12 = Client ('Juan', 'Sekundo', 54313)
  
  print(client1.client_info())
  alior.add_client(client1)
  alior.add_client(client2)
  print(client1.client_info())
  print(client1.bank)
  print(alior.clients)

  print(client1.cash, client2.cash)
  alior.transfer(client1, client2, 1000)
  print(client1.cash, client2.cash)

  print(client1.cash)
  alior.withdrawal(client1, 200)
  print(client1.cash)

  alior.change_bank(client1, pekao)
  print(client1.bank)
  print(alior.clients)
  print(pekao.clients)

