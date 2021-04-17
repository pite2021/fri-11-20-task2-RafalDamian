class Bank:

  def __init__(self, name, interest):
    self.name = name.title()
    self.interest = interest
    self.clients = []

  def add_client(self, client):
    client.bank = self.name
    self.clients.append(client.client_info())

  def delete_client(self, client):
    self.clients.remove(client.client_info)

  def give_credit(self, client, ammount):
    if client.client_info() in self.clients:
      client.cash += ammount
      client.add_credit(self.name, self.interest, self.ammount)


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

  def transfer(self, target, ammount):
    self.cash -= ammount
    target.cash += ammount

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

  maciek = Client('Maciek', 'Kazimierczak', 5000)
  kopec = Client('Pawel', 'Kopec', 2137)
  cholda = Client ('Lukas', 'Cholda', 6900)

  print(maciek.client_info)
  alior.add_client(maciek)
  print(maciek.client_info)
  print(maciek.bank)
