#FILA: Lista linear de informação, em que o mecanismo de recuperação de seus elementos respeita a regra FIFO (First in first out), ou seja o **primeiro elemento a entrar é o primeiro elemento a sair**.
class fila():
  def __init__(self,capacidade=10):
    self.fila = []
    self.max = capacidade
    self.prox = 0
    pass

  def inserir(self,item):
    if self.prox<self.max:
      print('Item %d inserido na posição %d'%(item,self.prox))
      self.prox +=1
      self.fila.append(item)
    else:
      print('Fila já está cheia, item %d não pode ser inserido'%(item))
    pass

  def remover(self):
    if self.prox>0:
      print('Item %d removido na posição 0'%(self.fila[0]))
      self.prox -=1
      self.fila.pop(0)
    else:
      print('Fila está vazia, não é possivel remover')
    pass


#PILHA: Lista linear de informação, em que o mecanismo de recuperação de seus elementos respeita a regra LIFO (Last in first out), ou seja o **ultimo elemento a entrar é o primeiro elemento a sair**.
class pilha():
  def __init__(self, capacidade=10):
    self.pilha = []
    self.max = capacidade
    self.topo = 0
    pass

  def empilhar(self,item):
    if self.topo<self.max:
      print('Item %d empilhado no topo da fila %d'%(item,self.topo))
      self.topo +=1
      self.pilha.append(item)
    else:
      print('Pilha já está cheia, item %d não pode ser empilhado'%(item))
    pass

  def desempilhar(self):
    if self.topo>0:
      print('Item %d desempilhado do topo da fila %d'%(self.pilha[-1],self.topo))
      self.topo -=1
      self.pilha.pop()
    else:
      print('Pilha está vazia, não é possivel desempilhar')
    pass

#LISTA: Lista encadeada onde a informação pode ser acessada randomicamente, desde que se tenha sua localização. Porem são acessados em sequencia, pois **cada item contem uma informação e um elo de ligação ao proximo item da cadeia**.
class node():
  def __init__(self, item=0, next=None):
    self.item = item
    self.next = next
    pass

  def __repr__(self):
    return self.item, self.next
class lista_encadeada(node):
  def __init__(self):
    self.head = None
    self._size = 0
    pass

  def add(self, item):
    if self.head:
      end = self.head
      while(end.next):
        end = end.next
      end.next = node(item)
    else:
      self.head = node(item)
    self._size += 1

  def _getNode(self,index):
    end = self.head
    for i in range(index):
      if end:
        end = end.next
      else:
        raise IndexError("Index fora da lista")
    return end

  def __getitem__(self, index):
    end = self._getNode(index)
    if end:
      return end.item
    else:
      raise IndexError("Index fora da lista")

  def __setitem__(self, index, item):
    end = self._getNode(index)
    if end:
      end.item = item
    else:
      raise IndexError("Index fora da lista")
    pass

  def insert(self, index, item):
    node = node(item)
    if index == 0:
      node.next = self.head
      self.head = node
    else:
      end = self._getNode(index-1)
      node.next = end.next
      end.next = node
    pass

  def sort(self,item):
    end = self.head
    index = 0
    while end:
      if end.item == item:
        return index
      else:
        end = end.next
      index+=1
    raise ValueError ("{} não está na lista".format(item))

  def __len__(self):
    return self._size

  def __repr__(self):
    return
