class Denigma.Member extends Batman.Model
  @serializeAsForm: false
  @encode 'id','name','surname','organization','age','salary'

  @validate 'id', numeric: true
  @validate 'age', numeric: true
  @validate 'salary', numeric: true

  @persist Batman.DjangoStorage

  @storageKey: 'member'

  @url: 'grids/models/member'
