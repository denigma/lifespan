class Denigma.Member extends Batman.Model

  @encode 'id','name','surname','organization','age','salary'

  @persist Batman.RestStorage

  @storageKey: 'member'

  @url: 'grids/models/member'
