

class Bank:

  def __init__(self, name, interest):
    self.name = name.title()
    self.interest = interest
    self.clients = []
  
  def add_client(self, client):
    client.bank = self.name
    self.clients.append(client)

  def delete_client(self, client):
    if client in self.clients:
      client.bank = 'no bank'
      self.clients.remove(client)

  def give_credit(self, client, ammount):
    if client in self.clients:
      client.cash += ammount
      client.add_credit(self.name, self.interest, self.ammount)

  def transfer(self, client, target, ammount):
    if client in self.clients:
      client.cash -= ammount
      target.cash += ammount
      
  def withdrawal(self, client, ammount):
    if client in self.clients:
      client.cash -= ammount

  def describe_clients(self):
    for customer in self.clients:
      return customer.client_info()


class Client:

  def __init__(self, name, surname, cash=2000):
    self.name = name.title()
    self.surname = surname.title()
    self.cash = cash
    self.bank = 'no bank'
    self.credit_info = []

  def add_credit(self, bank_name, interest, ammount):
    self.credit_info.append(
      {
      'bank' : bank_name,
      'ammount' : ammount,
      'interest' : interest
      }
    )

  def client_info(self):
    return {
        'name' : self.name,
        'surname' : self.surname,
        'cash' : self.cash,
        'bank' : self.bank,
        'credits' : self.credit_info
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
  print(alior.clients.client_info())
  alior.delete_client(client1)
  print(alior.clients.client_info())