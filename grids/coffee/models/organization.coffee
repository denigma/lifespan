class Denigma.Organization extends Batman.Model
  serializeAsForm: false
  @serializeAsForm: false #do not remember if it is static or normal property
  @primaryKey: 'id'
  #@hasMany "members", {saveInline:false,autoload:true,inverseOf: 'organization', foreignKey:'organization'}

  @encode 'id','name','description'

  @validate 'id', numeric: true

  @persist Batman.DjangoStorage

  @storageKey: 'organizatino'

  @url: 'grids/models/organization'
