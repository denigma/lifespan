class Denigma.Member extends Batman.Model
  serializeAsForm: false
  @serializeAsForm: false #do not remember if it is static or normal property

  #@belongsTo 'organization', {saveInline:true,autoload:true,inverseOf: 'member'}

  @encode 'id','name','surname','age','salary', 'organization'

  @validate 'id', numeric: true
  @validate 'age', numeric: true
  @validate 'salary', numeric: true

  @persist Batman.DjangoStorage

  @storageKey: 'member'

  @url: 'grids/models/member'
