class Denigma.Member extends Batman.Model
  serializeAsForm: false
  @serializeAsForm: false #do not remember if it is static or normal property

  @encode 'id','name','surname','organization','age','salary'

  @validate 'id', numeric: true
  @validate 'age', numeric: true
  @validate 'salary', numeric: true

  @persist Batman.DjangoStorage

  @storageKey: 'member'

  @url: 'grids/models/member'
