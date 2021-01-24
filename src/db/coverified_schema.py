import sgqlc.types
import sgqlc.types.datetime

coverified_schema = sgqlc.types.Schema()

########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean


class CacheControlScope(sgqlc.types.Enum):
    __schema__ = coverified_schema
    __choices__ = ('PUBLIC', 'PRIVATE')


DateTime = sgqlc.types.datetime.DateTime

Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int


class JSON(sgqlc.types.Scalar):
    __schema__ = coverified_schema


class SortEntriesBy(sgqlc.types.Enum):
    __schema__ = coverified_schema
    __choices__ = ('id_ASC', 'id_DESC', 'publishDate_ASC', 'publishDate_DESC', 'title_ASC', 'title_DESC', 'content_ASC',
                   'content_DESC', 'url_ASC', 'url_DESC', 'tags_ASC', 'tags_DESC', 'language_ASC', 'language_DESC',
                   'source_ASC', 'source_DESC', 'updatedAt_ASC', 'updatedAt_DESC', 'createdAt_ASC', 'createdAt_DESC')


class SortGeoLocationsBy(sgqlc.types.Enum):
    __schema__ = coverified_schema
    __choices__ = (
        'id_ASC', 'id_DESC', 'name_ASC', 'name_DESC', 'radius_ASC', 'radius_DESC', 'updatedAt_ASC', 'updatedAt_DESC',
        'createdAt_ASC', 'createdAt_DESC')


class SortLanguagesBy(sgqlc.types.Enum):
    __schema__ = coverified_schema
    __choices__ = (
        'id_ASC', 'id_DESC', 'name_ASC', 'name_DESC', 'updatedAt_ASC', 'updatedAt_DESC', 'createdAt_ASC',
        'createdAt_DESC')


class SortOrganizationsBy(sgqlc.types.Enum):
    __schema__ = coverified_schema
    __choices__ = (
        'id_ASC', 'id_DESC', 'name_ASC', 'name_DESC', 'updatedAt_ASC', 'updatedAt_DESC', 'createdAt_ASC',
        'createdAt_DESC')


class SortSourcesBy(sgqlc.types.Enum):
    __schema__ = coverified_schema
    __choices__ = ('id_ASC', 'id_DESC', 'name_ASC', 'name_DESC', 'url_ASC', 'url_DESC', 'location_ASC', 'location_DESC',
                   'description_ASC', 'description_DESC', 'updatedAt_ASC', 'updatedAt_DESC', 'createdAt_ASC',
                   'createdAt_DESC')


class SortTagsBy(sgqlc.types.Enum):
    __schema__ = coverified_schema
    __choices__ = ('id_ASC', 'id_DESC', 'name_ASC', 'name_DESC', 'language_ASC', 'language_DESC', 'description_ASC',
                   'description_DESC', 'relevance_ASC', 'relevance_DESC', 'updatedAt_ASC', 'updatedAt_DESC',
                   'createdAt_ASC', 'createdAt_DESC')


class SortUsersBy(sgqlc.types.Enum):
    __schema__ = coverified_schema
    __choices__ = (
        'id_ASC', 'id_DESC', 'name_ASC', 'name_DESC', 'email_ASC', 'email_DESC', 'isAdmin_ASC', 'isAdmin_DESC',
        'organization_ASC', 'organization_DESC', 'updatedAt_ASC', 'updatedAt_DESC', 'createdAt_ASC', 'createdAt_DESC')


class SortWidgetsBy(sgqlc.types.Enum):
    __schema__ = coverified_schema
    __choices__ = (
        'id_ASC', 'id_DESC', 'name_ASC', 'name_DESC', 'organization_ASC', 'organization_DESC', 'language_ASC',
        'language_DESC', 'sources_ASC', 'sources_DESC', 'updatedAt_ASC', 'updatedAt_DESC', 'createdAt_ASC',
        'createdAt_DESC')


String = sgqlc.types.String


class Upload(sgqlc.types.Scalar):
    __schema__ = coverified_schema


########################################################################
# Input Objects
########################################################################
class CloudinaryImageFormat(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = (
        'pretty_name', 'width', 'height', 'crop', 'aspect_ratio', 'gravity', 'zoom', 'x', 'y', 'format', 'fetch_format',
        'quality', 'radius', 'angle', 'effect', 'opacity', 'border', 'background', 'overlay', 'underlay',
        'default_image',
        'delay', 'color', 'color_space', 'dpr', 'page', 'density', 'flags', 'transformation')
    pretty_name = sgqlc.types.Field(String, graphql_name='prettyName')
    width = sgqlc.types.Field(String, graphql_name='width')
    height = sgqlc.types.Field(String, graphql_name='height')
    crop = sgqlc.types.Field(String, graphql_name='crop')
    aspect_ratio = sgqlc.types.Field(String, graphql_name='aspect_ratio')
    gravity = sgqlc.types.Field(String, graphql_name='gravity')
    zoom = sgqlc.types.Field(String, graphql_name='zoom')
    x = sgqlc.types.Field(String, graphql_name='x')
    y = sgqlc.types.Field(String, graphql_name='y')
    format = sgqlc.types.Field(String, graphql_name='format')
    fetch_format = sgqlc.types.Field(String, graphql_name='fetch_format')
    quality = sgqlc.types.Field(String, graphql_name='quality')
    radius = sgqlc.types.Field(String, graphql_name='radius')
    angle = sgqlc.types.Field(String, graphql_name='angle')
    effect = sgqlc.types.Field(String, graphql_name='effect')
    opacity = sgqlc.types.Field(String, graphql_name='opacity')
    border = sgqlc.types.Field(String, graphql_name='border')
    background = sgqlc.types.Field(String, graphql_name='background')
    overlay = sgqlc.types.Field(String, graphql_name='overlay')
    underlay = sgqlc.types.Field(String, graphql_name='underlay')
    default_image = sgqlc.types.Field(String, graphql_name='default_image')
    delay = sgqlc.types.Field(String, graphql_name='delay')
    color = sgqlc.types.Field(String, graphql_name='color')
    color_space = sgqlc.types.Field(String, graphql_name='color_space')
    dpr = sgqlc.types.Field(String, graphql_name='dpr')
    page = sgqlc.types.Field(String, graphql_name='page')
    density = sgqlc.types.Field(String, graphql_name='density')
    flags = sgqlc.types.Field(String, graphql_name='flags')
    transformation = sgqlc.types.Field(String, graphql_name='transformation')


class EntriesCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field('EntryCreateInput', graphql_name='data')


class EntriesUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id', 'data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    data = sgqlc.types.Field('EntryUpdateInput', graphql_name='data')


class EntryCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('publish_date', 'title', 'image', 'content', 'url', 'tags', 'language', 'source')
    publish_date = sgqlc.types.Field(String, graphql_name='publishDate')
    title = sgqlc.types.Field(String, graphql_name='title')
    image = sgqlc.types.Field(Upload, graphql_name='image')
    content = sgqlc.types.Field(String, graphql_name='content')
    url = sgqlc.types.Field(String, graphql_name='url')
    tags = sgqlc.types.Field('TagRelateToManyInput', graphql_name='tags')
    language = sgqlc.types.Field('LanguageRelateToOneInput', graphql_name='language')
    source = sgqlc.types.Field('SourceRelateToOneInput', graphql_name='source')


class EntryUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('publish_date', 'title', 'image', 'content', 'url', 'tags', 'language', 'source')
    publish_date = sgqlc.types.Field(String, graphql_name='publishDate')
    title = sgqlc.types.Field(String, graphql_name='title')
    image = sgqlc.types.Field(Upload, graphql_name='image')
    content = sgqlc.types.Field(String, graphql_name='content')
    url = sgqlc.types.Field(String, graphql_name='url')
    tags = sgqlc.types.Field('TagRelateToManyInput', graphql_name='tags')
    language = sgqlc.types.Field('LanguageRelateToOneInput', graphql_name='language')
    source = sgqlc.types.Field('SourceRelateToOneInput', graphql_name='source')


class EntryWhereInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = (
        'and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'publish_date', 'publish_date_not', 'publish_date_lt',
        'publish_date_lte', 'publish_date_gt', 'publish_date_gte', 'publish_date_in', 'publish_date_not_in', 'title',
        'title_not', 'title_contains', 'title_not_contains', 'title_starts_with', 'title_not_starts_with',
        'title_ends_with', 'title_not_ends_with', 'title_i', 'title_not_i', 'title_contains_i', 'title_not_contains_i',
        'title_starts_with_i', 'title_not_starts_with_i', 'title_ends_with_i', 'title_not_ends_with_i', 'title_in',
        'title_not_in', 'image', 'image_not', 'image_in', 'image_not_in', 'content', 'content_not', 'content_contains',
        'content_not_contains', 'content_starts_with', 'content_not_starts_with', 'content_ends_with',
        'content_not_ends_with', 'content_i', 'content_not_i', 'content_contains_i', 'content_not_contains_i',
        'content_starts_with_i', 'content_not_starts_with_i', 'content_ends_with_i', 'content_not_ends_with_i',
        'content_in', 'content_not_in', 'url', 'url_not', 'url_contains', 'url_not_contains', 'url_starts_with',
        'url_not_starts_with', 'url_ends_with', 'url_not_ends_with', 'url_i', 'url_not_i', 'url_contains_i',
        'url_not_contains_i', 'url_starts_with_i', 'url_not_starts_with_i', 'url_ends_with_i', 'url_not_ends_with_i',
        'url_in', 'url_not_in', 'tags_every', 'tags_some', 'tags_none', 'language', 'language_is_null', 'source',
        'source_is_null', 'updated_at', 'updated_at_not', 'updated_at_lt', 'updated_at_lte', 'updated_at_gt',
        'updated_at_gte', 'updated_at_in', 'updated_at_not_in', 'created_at', 'created_at_not', 'created_at_lt',
        'created_at_lte', 'created_at_gt', 'created_at_gte', 'created_at_in', 'created_at_not_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('EntryWhereInput'), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('EntryWhereInput'), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_not_in')
    publish_date = sgqlc.types.Field(String, graphql_name='publishDate')
    publish_date_not = sgqlc.types.Field(String, graphql_name='publishDate_not')
    publish_date_lt = sgqlc.types.Field(String, graphql_name='publishDate_lt')
    publish_date_lte = sgqlc.types.Field(String, graphql_name='publishDate_lte')
    publish_date_gt = sgqlc.types.Field(String, graphql_name='publishDate_gt')
    publish_date_gte = sgqlc.types.Field(String, graphql_name='publishDate_gte')
    publish_date_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publishDate_in')
    publish_date_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publishDate_not_in')
    title = sgqlc.types.Field(String, graphql_name='title')
    title_not = sgqlc.types.Field(String, graphql_name='title_not')
    title_contains = sgqlc.types.Field(String, graphql_name='title_contains')
    title_not_contains = sgqlc.types.Field(String, graphql_name='title_not_contains')
    title_starts_with = sgqlc.types.Field(String, graphql_name='title_starts_with')
    title_not_starts_with = sgqlc.types.Field(String, graphql_name='title_not_starts_with')
    title_ends_with = sgqlc.types.Field(String, graphql_name='title_ends_with')
    title_not_ends_with = sgqlc.types.Field(String, graphql_name='title_not_ends_with')
    title_i = sgqlc.types.Field(String, graphql_name='title_i')
    title_not_i = sgqlc.types.Field(String, graphql_name='title_not_i')
    title_contains_i = sgqlc.types.Field(String, graphql_name='title_contains_i')
    title_not_contains_i = sgqlc.types.Field(String, graphql_name='title_not_contains_i')
    title_starts_with_i = sgqlc.types.Field(String, graphql_name='title_starts_with_i')
    title_not_starts_with_i = sgqlc.types.Field(String, graphql_name='title_not_starts_with_i')
    title_ends_with_i = sgqlc.types.Field(String, graphql_name='title_ends_with_i')
    title_not_ends_with_i = sgqlc.types.Field(String, graphql_name='title_not_ends_with_i')
    title_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='title_in')
    title_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='title_not_in')
    image = sgqlc.types.Field(String, graphql_name='image')
    image_not = sgqlc.types.Field(String, graphql_name='image_not')
    image_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='image_in')
    image_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='image_not_in')
    content = sgqlc.types.Field(String, graphql_name='content')
    content_not = sgqlc.types.Field(String, graphql_name='content_not')
    content_contains = sgqlc.types.Field(String, graphql_name='content_contains')
    content_not_contains = sgqlc.types.Field(String, graphql_name='content_not_contains')
    content_starts_with = sgqlc.types.Field(String, graphql_name='content_starts_with')
    content_not_starts_with = sgqlc.types.Field(String, graphql_name='content_not_starts_with')
    content_ends_with = sgqlc.types.Field(String, graphql_name='content_ends_with')
    content_not_ends_with = sgqlc.types.Field(String, graphql_name='content_not_ends_with')
    content_i = sgqlc.types.Field(String, graphql_name='content_i')
    content_not_i = sgqlc.types.Field(String, graphql_name='content_not_i')
    content_contains_i = sgqlc.types.Field(String, graphql_name='content_contains_i')
    content_not_contains_i = sgqlc.types.Field(String, graphql_name='content_not_contains_i')
    content_starts_with_i = sgqlc.types.Field(String, graphql_name='content_starts_with_i')
    content_not_starts_with_i = sgqlc.types.Field(String, graphql_name='content_not_starts_with_i')
    content_ends_with_i = sgqlc.types.Field(String, graphql_name='content_ends_with_i')
    content_not_ends_with_i = sgqlc.types.Field(String, graphql_name='content_not_ends_with_i')
    content_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='content_in')
    content_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='content_not_in')
    url = sgqlc.types.Field(String, graphql_name='url')
    url_not = sgqlc.types.Field(String, graphql_name='url_not')
    url_contains = sgqlc.types.Field(String, graphql_name='url_contains')
    url_not_contains = sgqlc.types.Field(String, graphql_name='url_not_contains')
    url_starts_with = sgqlc.types.Field(String, graphql_name='url_starts_with')
    url_not_starts_with = sgqlc.types.Field(String, graphql_name='url_not_starts_with')
    url_ends_with = sgqlc.types.Field(String, graphql_name='url_ends_with')
    url_not_ends_with = sgqlc.types.Field(String, graphql_name='url_not_ends_with')
    url_i = sgqlc.types.Field(String, graphql_name='url_i')
    url_not_i = sgqlc.types.Field(String, graphql_name='url_not_i')
    url_contains_i = sgqlc.types.Field(String, graphql_name='url_contains_i')
    url_not_contains_i = sgqlc.types.Field(String, graphql_name='url_not_contains_i')
    url_starts_with_i = sgqlc.types.Field(String, graphql_name='url_starts_with_i')
    url_not_starts_with_i = sgqlc.types.Field(String, graphql_name='url_not_starts_with_i')
    url_ends_with_i = sgqlc.types.Field(String, graphql_name='url_ends_with_i')
    url_not_ends_with_i = sgqlc.types.Field(String, graphql_name='url_not_ends_with_i')
    url_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='url_in')
    url_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='url_not_in')
    tags_every = sgqlc.types.Field('TagWhereInput', graphql_name='tags_every')
    tags_some = sgqlc.types.Field('TagWhereInput', graphql_name='tags_some')
    tags_none = sgqlc.types.Field('TagWhereInput', graphql_name='tags_none')
    language = sgqlc.types.Field('LanguageWhereInput', graphql_name='language')
    language_is_null = sgqlc.types.Field(Boolean, graphql_name='language_is_null')
    source = sgqlc.types.Field('SourceWhereInput', graphql_name='source')
    source_is_null = sgqlc.types.Field(Boolean, graphql_name='source_is_null')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    updated_at_not = sgqlc.types.Field(DateTime, graphql_name='updatedAt_not')
    updated_at_lt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lt')
    updated_at_lte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lte')
    updated_at_gt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gt')
    updated_at_gte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gte')
    updated_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_in')
    updated_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_not_in')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    created_at_not = sgqlc.types.Field(DateTime, graphql_name='createdAt_not')
    created_at_lt = sgqlc.types.Field(DateTime, graphql_name='createdAt_lt')
    created_at_lte = sgqlc.types.Field(DateTime, graphql_name='createdAt_lte')
    created_at_gt = sgqlc.types.Field(DateTime, graphql_name='createdAt_gt')
    created_at_gte = sgqlc.types.Field(DateTime, graphql_name='createdAt_gte')
    created_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_in')
    created_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_not_in')


class EntryWhereUniqueInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class GeoLocationCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name', 'location', 'radius')
    name = sgqlc.types.Field(String, graphql_name='name')
    location = sgqlc.types.Field(String, graphql_name='location')
    radius = sgqlc.types.Field(Float, graphql_name='radius')


class GeoLocationRelateToOneInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('create', 'connect', 'disconnect', 'disconnect_all')
    create = sgqlc.types.Field(GeoLocationCreateInput, graphql_name='create')
    connect = sgqlc.types.Field('GeoLocationWhereUniqueInput', graphql_name='connect')
    disconnect = sgqlc.types.Field('GeoLocationWhereUniqueInput', graphql_name='disconnect')
    disconnect_all = sgqlc.types.Field(Boolean, graphql_name='disconnectAll')


class GeoLocationUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name', 'location', 'radius')
    name = sgqlc.types.Field(String, graphql_name='name')
    location = sgqlc.types.Field(String, graphql_name='location')
    radius = sgqlc.types.Field(Float, graphql_name='radius')


class GeoLocationWhereInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = (
        'and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'name', 'name_not', 'name_contains', 'name_not_contains',
        'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'name_i', 'name_not_i',
        'name_contains_i', 'name_not_contains_i', 'name_starts_with_i', 'name_not_starts_with_i', 'name_ends_with_i',
        'name_not_ends_with_i', 'name_in', 'name_not_in', 'location', 'location_not', 'location_in', 'location_not_in',
        'radius', 'radius_not', 'radius_lt', 'radius_lte', 'radius_gt', 'radius_gte', 'radius_in', 'radius_not_in',
        'updated_at', 'updated_at_not', 'updated_at_lt', 'updated_at_lte', 'updated_at_gt', 'updated_at_gte',
        'updated_at_in', 'updated_at_not_in', 'created_at', 'created_at_not', 'created_at_lt', 'created_at_lte',
        'created_at_gt', 'created_at_gte', 'created_at_in', 'created_at_not_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('GeoLocationWhereInput'), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('GeoLocationWhereInput'), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_i = sgqlc.types.Field(String, graphql_name='name_i')
    name_not_i = sgqlc.types.Field(String, graphql_name='name_not_i')
    name_contains_i = sgqlc.types.Field(String, graphql_name='name_contains_i')
    name_not_contains_i = sgqlc.types.Field(String, graphql_name='name_not_contains_i')
    name_starts_with_i = sgqlc.types.Field(String, graphql_name='name_starts_with_i')
    name_not_starts_with_i = sgqlc.types.Field(String, graphql_name='name_not_starts_with_i')
    name_ends_with_i = sgqlc.types.Field(String, graphql_name='name_ends_with_i')
    name_not_ends_with_i = sgqlc.types.Field(String, graphql_name='name_not_ends_with_i')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_not_in')
    location = sgqlc.types.Field(String, graphql_name='location')
    location_not = sgqlc.types.Field(String, graphql_name='location_not')
    location_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='location_in')
    location_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='location_not_in')
    radius = sgqlc.types.Field(Float, graphql_name='radius')
    radius_not = sgqlc.types.Field(Float, graphql_name='radius_not')
    radius_lt = sgqlc.types.Field(Float, graphql_name='radius_lt')
    radius_lte = sgqlc.types.Field(Float, graphql_name='radius_lte')
    radius_gt = sgqlc.types.Field(Float, graphql_name='radius_gt')
    radius_gte = sgqlc.types.Field(Float, graphql_name='radius_gte')
    radius_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='radius_in')
    radius_not_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='radius_not_in')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    updated_at_not = sgqlc.types.Field(DateTime, graphql_name='updatedAt_not')
    updated_at_lt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lt')
    updated_at_lte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lte')
    updated_at_gt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gt')
    updated_at_gte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gte')
    updated_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_in')
    updated_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_not_in')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    created_at_not = sgqlc.types.Field(DateTime, graphql_name='createdAt_not')
    created_at_lt = sgqlc.types.Field(DateTime, graphql_name='createdAt_lt')
    created_at_lte = sgqlc.types.Field(DateTime, graphql_name='createdAt_lte')
    created_at_gt = sgqlc.types.Field(DateTime, graphql_name='createdAt_gt')
    created_at_gte = sgqlc.types.Field(DateTime, graphql_name='createdAt_gte')
    created_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_in')
    created_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_not_in')


class GeoLocationWhereUniqueInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class GeoLocationsCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(GeoLocationCreateInput, graphql_name='data')


class GeoLocationsUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id', 'data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    data = sgqlc.types.Field(GeoLocationUpdateInput, graphql_name='data')


class LanguageCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')


class LanguageRelateToOneInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('create', 'connect', 'disconnect', 'disconnect_all')
    create = sgqlc.types.Field(LanguageCreateInput, graphql_name='create')
    connect = sgqlc.types.Field('LanguageWhereUniqueInput', graphql_name='connect')
    disconnect = sgqlc.types.Field('LanguageWhereUniqueInput', graphql_name='disconnect')
    disconnect_all = sgqlc.types.Field(Boolean, graphql_name='disconnectAll')


class LanguageUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')


class LanguageWhereInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = (
        'and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'name', 'name_not', 'name_contains', 'name_not_contains',
        'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'name_i', 'name_not_i',
        'name_contains_i', 'name_not_contains_i', 'name_starts_with_i', 'name_not_starts_with_i', 'name_ends_with_i',
        'name_not_ends_with_i', 'name_in', 'name_not_in', 'updated_at', 'updated_at_not', 'updated_at_lt',
        'updated_at_lte',
        'updated_at_gt', 'updated_at_gte', 'updated_at_in', 'updated_at_not_in', 'created_at', 'created_at_not',
        'created_at_lt', 'created_at_lte', 'created_at_gt', 'created_at_gte', 'created_at_in', 'created_at_not_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('LanguageWhereInput'), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('LanguageWhereInput'), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_i = sgqlc.types.Field(String, graphql_name='name_i')
    name_not_i = sgqlc.types.Field(String, graphql_name='name_not_i')
    name_contains_i = sgqlc.types.Field(String, graphql_name='name_contains_i')
    name_not_contains_i = sgqlc.types.Field(String, graphql_name='name_not_contains_i')
    name_starts_with_i = sgqlc.types.Field(String, graphql_name='name_starts_with_i')
    name_not_starts_with_i = sgqlc.types.Field(String, graphql_name='name_not_starts_with_i')
    name_ends_with_i = sgqlc.types.Field(String, graphql_name='name_ends_with_i')
    name_not_ends_with_i = sgqlc.types.Field(String, graphql_name='name_not_ends_with_i')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_not_in')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    updated_at_not = sgqlc.types.Field(DateTime, graphql_name='updatedAt_not')
    updated_at_lt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lt')
    updated_at_lte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lte')
    updated_at_gt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gt')
    updated_at_gte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gte')
    updated_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_in')
    updated_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_not_in')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    created_at_not = sgqlc.types.Field(DateTime, graphql_name='createdAt_not')
    created_at_lt = sgqlc.types.Field(DateTime, graphql_name='createdAt_lt')
    created_at_lte = sgqlc.types.Field(DateTime, graphql_name='createdAt_lte')
    created_at_gt = sgqlc.types.Field(DateTime, graphql_name='createdAt_gt')
    created_at_gte = sgqlc.types.Field(DateTime, graphql_name='createdAt_gte')
    created_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_in')
    created_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_not_in')


class LanguageWhereUniqueInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class LanguagesCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(LanguageCreateInput, graphql_name='data')


class LanguagesUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id', 'data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    data = sgqlc.types.Field(LanguageUpdateInput, graphql_name='data')


class OrganizationCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')


class OrganizationRelateToOneInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('create', 'connect', 'disconnect', 'disconnect_all')
    create = sgqlc.types.Field(OrganizationCreateInput, graphql_name='create')
    connect = sgqlc.types.Field('OrganizationWhereUniqueInput', graphql_name='connect')
    disconnect = sgqlc.types.Field('OrganizationWhereUniqueInput', graphql_name='disconnect')
    disconnect_all = sgqlc.types.Field(Boolean, graphql_name='disconnectAll')


class OrganizationUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')


class OrganizationWhereInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = (
        'and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'name', 'name_not', 'name_contains', 'name_not_contains',
        'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'name_i', 'name_not_i',
        'name_contains_i', 'name_not_contains_i', 'name_starts_with_i', 'name_not_starts_with_i', 'name_ends_with_i',
        'name_not_ends_with_i', 'name_in', 'name_not_in', 'updated_at', 'updated_at_not', 'updated_at_lt',
        'updated_at_lte',
        'updated_at_gt', 'updated_at_gte', 'updated_at_in', 'updated_at_not_in', 'created_at', 'created_at_not',
        'created_at_lt', 'created_at_lte', 'created_at_gt', 'created_at_gte', 'created_at_in', 'created_at_not_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('OrganizationWhereInput'), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('OrganizationWhereInput'), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_i = sgqlc.types.Field(String, graphql_name='name_i')
    name_not_i = sgqlc.types.Field(String, graphql_name='name_not_i')
    name_contains_i = sgqlc.types.Field(String, graphql_name='name_contains_i')
    name_not_contains_i = sgqlc.types.Field(String, graphql_name='name_not_contains_i')
    name_starts_with_i = sgqlc.types.Field(String, graphql_name='name_starts_with_i')
    name_not_starts_with_i = sgqlc.types.Field(String, graphql_name='name_not_starts_with_i')
    name_ends_with_i = sgqlc.types.Field(String, graphql_name='name_ends_with_i')
    name_not_ends_with_i = sgqlc.types.Field(String, graphql_name='name_not_ends_with_i')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_not_in')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    updated_at_not = sgqlc.types.Field(DateTime, graphql_name='updatedAt_not')
    updated_at_lt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lt')
    updated_at_lte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lte')
    updated_at_gt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gt')
    updated_at_gte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gte')
    updated_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_in')
    updated_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_not_in')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    created_at_not = sgqlc.types.Field(DateTime, graphql_name='createdAt_not')
    created_at_lt = sgqlc.types.Field(DateTime, graphql_name='createdAt_lt')
    created_at_lte = sgqlc.types.Field(DateTime, graphql_name='createdAt_lte')
    created_at_gt = sgqlc.types.Field(DateTime, graphql_name='createdAt_gt')
    created_at_gte = sgqlc.types.Field(DateTime, graphql_name='createdAt_gte')
    created_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_in')
    created_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_not_in')


class OrganizationWhereUniqueInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class OrganizationsCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(OrganizationCreateInput, graphql_name='data')


class OrganizationsUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id', 'data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    data = sgqlc.types.Field(OrganizationUpdateInput, graphql_name='data')


class SourceCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name', 'url', 'location', 'description')
    name = sgqlc.types.Field(String, graphql_name='name')
    url = sgqlc.types.Field(String, graphql_name='url')
    location = sgqlc.types.Field(GeoLocationRelateToOneInput, graphql_name='location')
    description = sgqlc.types.Field(String, graphql_name='description')


class SourceRelateToManyInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('create', 'connect', 'disconnect', 'disconnect_all')
    create = sgqlc.types.Field(sgqlc.types.list_of(SourceCreateInput), graphql_name='create')
    connect = sgqlc.types.Field(sgqlc.types.list_of('SourceWhereUniqueInput'), graphql_name='connect')
    disconnect = sgqlc.types.Field(sgqlc.types.list_of('SourceWhereUniqueInput'), graphql_name='disconnect')
    disconnect_all = sgqlc.types.Field(Boolean, graphql_name='disconnectAll')


class SourceRelateToOneInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('create', 'connect', 'disconnect', 'disconnect_all')
    create = sgqlc.types.Field(SourceCreateInput, graphql_name='create')
    connect = sgqlc.types.Field('SourceWhereUniqueInput', graphql_name='connect')
    disconnect = sgqlc.types.Field('SourceWhereUniqueInput', graphql_name='disconnect')
    disconnect_all = sgqlc.types.Field(Boolean, graphql_name='disconnectAll')


class SourceUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name', 'url', 'location', 'description')
    name = sgqlc.types.Field(String, graphql_name='name')
    url = sgqlc.types.Field(String, graphql_name='url')
    location = sgqlc.types.Field(GeoLocationRelateToOneInput, graphql_name='location')
    description = sgqlc.types.Field(String, graphql_name='description')


class SourceWhereInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = (
        'and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'name', 'name_not', 'name_contains', 'name_not_contains',
        'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'name_i', 'name_not_i',
        'name_contains_i', 'name_not_contains_i', 'name_starts_with_i', 'name_not_starts_with_i', 'name_ends_with_i',
        'name_not_ends_with_i', 'name_in', 'name_not_in', 'url', 'url_not', 'url_contains', 'url_not_contains',
        'url_starts_with', 'url_not_starts_with', 'url_ends_with', 'url_not_ends_with', 'url_i', 'url_not_i',
        'url_contains_i', 'url_not_contains_i', 'url_starts_with_i', 'url_not_starts_with_i', 'url_ends_with_i',
        'url_not_ends_with_i', 'url_in', 'url_not_in', 'location', 'location_is_null', 'description', 'description_not',
        'description_contains', 'description_not_contains', 'description_starts_with', 'description_not_starts_with',
        'description_ends_with', 'description_not_ends_with', 'description_i', 'description_not_i',
        'description_contains_i', 'description_not_contains_i', 'description_starts_with_i',
        'description_not_starts_with_i', 'description_ends_with_i', 'description_not_ends_with_i', 'description_in',
        'description_not_in', 'updated_at', 'updated_at_not', 'updated_at_lt', 'updated_at_lte', 'updated_at_gt',
        'updated_at_gte', 'updated_at_in', 'updated_at_not_in', 'created_at', 'created_at_not', 'created_at_lt',
        'created_at_lte', 'created_at_gt', 'created_at_gte', 'created_at_in', 'created_at_not_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('SourceWhereInput'), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('SourceWhereInput'), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_i = sgqlc.types.Field(String, graphql_name='name_i')
    name_not_i = sgqlc.types.Field(String, graphql_name='name_not_i')
    name_contains_i = sgqlc.types.Field(String, graphql_name='name_contains_i')
    name_not_contains_i = sgqlc.types.Field(String, graphql_name='name_not_contains_i')
    name_starts_with_i = sgqlc.types.Field(String, graphql_name='name_starts_with_i')
    name_not_starts_with_i = sgqlc.types.Field(String, graphql_name='name_not_starts_with_i')
    name_ends_with_i = sgqlc.types.Field(String, graphql_name='name_ends_with_i')
    name_not_ends_with_i = sgqlc.types.Field(String, graphql_name='name_not_ends_with_i')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_not_in')
    url = sgqlc.types.Field(String, graphql_name='url')
    url_not = sgqlc.types.Field(String, graphql_name='url_not')
    url_contains = sgqlc.types.Field(String, graphql_name='url_contains')
    url_not_contains = sgqlc.types.Field(String, graphql_name='url_not_contains')
    url_starts_with = sgqlc.types.Field(String, graphql_name='url_starts_with')
    url_not_starts_with = sgqlc.types.Field(String, graphql_name='url_not_starts_with')
    url_ends_with = sgqlc.types.Field(String, graphql_name='url_ends_with')
    url_not_ends_with = sgqlc.types.Field(String, graphql_name='url_not_ends_with')
    url_i = sgqlc.types.Field(String, graphql_name='url_i')
    url_not_i = sgqlc.types.Field(String, graphql_name='url_not_i')
    url_contains_i = sgqlc.types.Field(String, graphql_name='url_contains_i')
    url_not_contains_i = sgqlc.types.Field(String, graphql_name='url_not_contains_i')
    url_starts_with_i = sgqlc.types.Field(String, graphql_name='url_starts_with_i')
    url_not_starts_with_i = sgqlc.types.Field(String, graphql_name='url_not_starts_with_i')
    url_ends_with_i = sgqlc.types.Field(String, graphql_name='url_ends_with_i')
    url_not_ends_with_i = sgqlc.types.Field(String, graphql_name='url_not_ends_with_i')
    url_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='url_in')
    url_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='url_not_in')
    location = sgqlc.types.Field(GeoLocationWhereInput, graphql_name='location')
    location_is_null = sgqlc.types.Field(Boolean, graphql_name='location_is_null')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_not = sgqlc.types.Field(String, graphql_name='description_not')
    description_contains = sgqlc.types.Field(String, graphql_name='description_contains')
    description_not_contains = sgqlc.types.Field(String, graphql_name='description_not_contains')
    description_starts_with = sgqlc.types.Field(String, graphql_name='description_starts_with')
    description_not_starts_with = sgqlc.types.Field(String, graphql_name='description_not_starts_with')
    description_ends_with = sgqlc.types.Field(String, graphql_name='description_ends_with')
    description_not_ends_with = sgqlc.types.Field(String, graphql_name='description_not_ends_with')
    description_i = sgqlc.types.Field(String, graphql_name='description_i')
    description_not_i = sgqlc.types.Field(String, graphql_name='description_not_i')
    description_contains_i = sgqlc.types.Field(String, graphql_name='description_contains_i')
    description_not_contains_i = sgqlc.types.Field(String, graphql_name='description_not_contains_i')
    description_starts_with_i = sgqlc.types.Field(String, graphql_name='description_starts_with_i')
    description_not_starts_with_i = sgqlc.types.Field(String, graphql_name='description_not_starts_with_i')
    description_ends_with_i = sgqlc.types.Field(String, graphql_name='description_ends_with_i')
    description_not_ends_with_i = sgqlc.types.Field(String, graphql_name='description_not_ends_with_i')
    description_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='description_in')
    description_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='description_not_in')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    updated_at_not = sgqlc.types.Field(DateTime, graphql_name='updatedAt_not')
    updated_at_lt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lt')
    updated_at_lte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lte')
    updated_at_gt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gt')
    updated_at_gte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gte')
    updated_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_in')
    updated_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_not_in')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    created_at_not = sgqlc.types.Field(DateTime, graphql_name='createdAt_not')
    created_at_lt = sgqlc.types.Field(DateTime, graphql_name='createdAt_lt')
    created_at_lte = sgqlc.types.Field(DateTime, graphql_name='createdAt_lte')
    created_at_gt = sgqlc.types.Field(DateTime, graphql_name='createdAt_gt')
    created_at_gte = sgqlc.types.Field(DateTime, graphql_name='createdAt_gte')
    created_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_in')
    created_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_not_in')


class SourceWhereUniqueInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class SourcesCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(SourceCreateInput, graphql_name='data')


class SourcesUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id', 'data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    data = sgqlc.types.Field(SourceUpdateInput, graphql_name='data')


class TagCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name', 'language', 'description', 'relevance', 'image')
    name = sgqlc.types.Field(String, graphql_name='name')
    language = sgqlc.types.Field(LanguageRelateToOneInput, graphql_name='language')
    description = sgqlc.types.Field(String, graphql_name='description')
    relevance = sgqlc.types.Field(Int, graphql_name='relevance')
    image = sgqlc.types.Field(Upload, graphql_name='image')


class TagRelateToManyInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('create', 'connect', 'disconnect', 'disconnect_all')
    create = sgqlc.types.Field(sgqlc.types.list_of(TagCreateInput), graphql_name='create')
    connect = sgqlc.types.Field(sgqlc.types.list_of('TagWhereUniqueInput'), graphql_name='connect')
    disconnect = sgqlc.types.Field(sgqlc.types.list_of('TagWhereUniqueInput'), graphql_name='disconnect')
    disconnect_all = sgqlc.types.Field(Boolean, graphql_name='disconnectAll')


class TagUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name', 'language', 'description', 'relevance', 'image')
    name = sgqlc.types.Field(String, graphql_name='name')
    language = sgqlc.types.Field(LanguageRelateToOneInput, graphql_name='language')
    description = sgqlc.types.Field(String, graphql_name='description')
    relevance = sgqlc.types.Field(Int, graphql_name='relevance')
    image = sgqlc.types.Field(Upload, graphql_name='image')


class TagWhereInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = (
        'and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'name', 'name_not', 'name_contains', 'name_not_contains',
        'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'name_i', 'name_not_i',
        'name_contains_i', 'name_not_contains_i', 'name_starts_with_i', 'name_not_starts_with_i', 'name_ends_with_i',
        'name_not_ends_with_i', 'name_in', 'name_not_in', 'language', 'language_is_null', 'description',
        'description_not',
        'description_contains', 'description_not_contains', 'description_starts_with', 'description_not_starts_with',
        'description_ends_with', 'description_not_ends_with', 'description_i', 'description_not_i',
        'description_contains_i', 'description_not_contains_i', 'description_starts_with_i',
        'description_not_starts_with_i', 'description_ends_with_i', 'description_not_ends_with_i', 'description_in',
        'description_not_in', 'relevance', 'relevance_not', 'relevance_lt', 'relevance_lte', 'relevance_gt',
        'relevance_gte', 'relevance_in', 'relevance_not_in', 'image', 'image_not', 'image_in', 'image_not_in',
        'updated_at',
        'updated_at_not', 'updated_at_lt', 'updated_at_lte', 'updated_at_gt', 'updated_at_gte', 'updated_at_in',
        'updated_at_not_in', 'created_at', 'created_at_not', 'created_at_lt', 'created_at_lte', 'created_at_gt',
        'created_at_gte', 'created_at_in', 'created_at_not_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('TagWhereInput'), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('TagWhereInput'), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_i = sgqlc.types.Field(String, graphql_name='name_i')
    name_not_i = sgqlc.types.Field(String, graphql_name='name_not_i')
    name_contains_i = sgqlc.types.Field(String, graphql_name='name_contains_i')
    name_not_contains_i = sgqlc.types.Field(String, graphql_name='name_not_contains_i')
    name_starts_with_i = sgqlc.types.Field(String, graphql_name='name_starts_with_i')
    name_not_starts_with_i = sgqlc.types.Field(String, graphql_name='name_not_starts_with_i')
    name_ends_with_i = sgqlc.types.Field(String, graphql_name='name_ends_with_i')
    name_not_ends_with_i = sgqlc.types.Field(String, graphql_name='name_not_ends_with_i')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_not_in')
    language = sgqlc.types.Field(LanguageWhereInput, graphql_name='language')
    language_is_null = sgqlc.types.Field(Boolean, graphql_name='language_is_null')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_not = sgqlc.types.Field(String, graphql_name='description_not')
    description_contains = sgqlc.types.Field(String, graphql_name='description_contains')
    description_not_contains = sgqlc.types.Field(String, graphql_name='description_not_contains')
    description_starts_with = sgqlc.types.Field(String, graphql_name='description_starts_with')
    description_not_starts_with = sgqlc.types.Field(String, graphql_name='description_not_starts_with')
    description_ends_with = sgqlc.types.Field(String, graphql_name='description_ends_with')
    description_not_ends_with = sgqlc.types.Field(String, graphql_name='description_not_ends_with')
    description_i = sgqlc.types.Field(String, graphql_name='description_i')
    description_not_i = sgqlc.types.Field(String, graphql_name='description_not_i')
    description_contains_i = sgqlc.types.Field(String, graphql_name='description_contains_i')
    description_not_contains_i = sgqlc.types.Field(String, graphql_name='description_not_contains_i')
    description_starts_with_i = sgqlc.types.Field(String, graphql_name='description_starts_with_i')
    description_not_starts_with_i = sgqlc.types.Field(String, graphql_name='description_not_starts_with_i')
    description_ends_with_i = sgqlc.types.Field(String, graphql_name='description_ends_with_i')
    description_not_ends_with_i = sgqlc.types.Field(String, graphql_name='description_not_ends_with_i')
    description_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='description_in')
    description_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='description_not_in')
    relevance = sgqlc.types.Field(Int, graphql_name='relevance')
    relevance_not = sgqlc.types.Field(Int, graphql_name='relevance_not')
    relevance_lt = sgqlc.types.Field(Int, graphql_name='relevance_lt')
    relevance_lte = sgqlc.types.Field(Int, graphql_name='relevance_lte')
    relevance_gt = sgqlc.types.Field(Int, graphql_name='relevance_gt')
    relevance_gte = sgqlc.types.Field(Int, graphql_name='relevance_gte')
    relevance_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='relevance_in')
    relevance_not_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='relevance_not_in')
    image = sgqlc.types.Field(String, graphql_name='image')
    image_not = sgqlc.types.Field(String, graphql_name='image_not')
    image_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='image_in')
    image_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='image_not_in')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    updated_at_not = sgqlc.types.Field(DateTime, graphql_name='updatedAt_not')
    updated_at_lt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lt')
    updated_at_lte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lte')
    updated_at_gt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gt')
    updated_at_gte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gte')
    updated_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_in')
    updated_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_not_in')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    created_at_not = sgqlc.types.Field(DateTime, graphql_name='createdAt_not')
    created_at_lt = sgqlc.types.Field(DateTime, graphql_name='createdAt_lt')
    created_at_lte = sgqlc.types.Field(DateTime, graphql_name='createdAt_lte')
    created_at_gt = sgqlc.types.Field(DateTime, graphql_name='createdAt_gt')
    created_at_gte = sgqlc.types.Field(DateTime, graphql_name='createdAt_gte')
    created_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_in')
    created_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_not_in')


class TagWhereUniqueInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class TagsCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(TagCreateInput, graphql_name='data')


class TagsUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id', 'data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    data = sgqlc.types.Field(TagUpdateInput, graphql_name='data')


class UserCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name', 'email', 'is_admin', 'password', 'organization')
    name = sgqlc.types.Field(String, graphql_name='name')
    email = sgqlc.types.Field(String, graphql_name='email')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')
    password = sgqlc.types.Field(String, graphql_name='password')
    organization = sgqlc.types.Field(OrganizationRelateToOneInput, graphql_name='organization')


class UserUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name', 'email', 'is_admin', 'password', 'organization')
    name = sgqlc.types.Field(String, graphql_name='name')
    email = sgqlc.types.Field(String, graphql_name='email')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')
    password = sgqlc.types.Field(String, graphql_name='password')
    organization = sgqlc.types.Field(OrganizationRelateToOneInput, graphql_name='organization')


class UserWhereInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = (
        'and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'name', 'name_not', 'name_contains', 'name_not_contains',
        'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'name_i', 'name_not_i',
        'name_contains_i', 'name_not_contains_i', 'name_starts_with_i', 'name_not_starts_with_i', 'name_ends_with_i',
        'name_not_ends_with_i', 'name_in', 'name_not_in', 'email', 'email_not', 'email_contains', 'email_not_contains',
        'email_starts_with', 'email_not_starts_with', 'email_ends_with', 'email_not_ends_with', 'email_i',
        'email_not_i',
        'email_contains_i', 'email_not_contains_i', 'email_starts_with_i', 'email_not_starts_with_i',
        'email_ends_with_i',
        'email_not_ends_with_i', 'email_in', 'email_not_in', 'is_admin', 'is_admin_not', 'password_is_set',
        'organization',
        'organization_is_null', 'updated_at', 'updated_at_not', 'updated_at_lt', 'updated_at_lte', 'updated_at_gt',
        'updated_at_gte', 'updated_at_in', 'updated_at_not_in', 'created_at', 'created_at_not', 'created_at_lt',
        'created_at_lte', 'created_at_gt', 'created_at_gte', 'created_at_in', 'created_at_not_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('UserWhereInput'), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('UserWhereInput'), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_i = sgqlc.types.Field(String, graphql_name='name_i')
    name_not_i = sgqlc.types.Field(String, graphql_name='name_not_i')
    name_contains_i = sgqlc.types.Field(String, graphql_name='name_contains_i')
    name_not_contains_i = sgqlc.types.Field(String, graphql_name='name_not_contains_i')
    name_starts_with_i = sgqlc.types.Field(String, graphql_name='name_starts_with_i')
    name_not_starts_with_i = sgqlc.types.Field(String, graphql_name='name_not_starts_with_i')
    name_ends_with_i = sgqlc.types.Field(String, graphql_name='name_ends_with_i')
    name_not_ends_with_i = sgqlc.types.Field(String, graphql_name='name_not_ends_with_i')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_not_in')
    email = sgqlc.types.Field(String, graphql_name='email')
    email_not = sgqlc.types.Field(String, graphql_name='email_not')
    email_contains = sgqlc.types.Field(String, graphql_name='email_contains')
    email_not_contains = sgqlc.types.Field(String, graphql_name='email_not_contains')
    email_starts_with = sgqlc.types.Field(String, graphql_name='email_starts_with')
    email_not_starts_with = sgqlc.types.Field(String, graphql_name='email_not_starts_with')
    email_ends_with = sgqlc.types.Field(String, graphql_name='email_ends_with')
    email_not_ends_with = sgqlc.types.Field(String, graphql_name='email_not_ends_with')
    email_i = sgqlc.types.Field(String, graphql_name='email_i')
    email_not_i = sgqlc.types.Field(String, graphql_name='email_not_i')
    email_contains_i = sgqlc.types.Field(String, graphql_name='email_contains_i')
    email_not_contains_i = sgqlc.types.Field(String, graphql_name='email_not_contains_i')
    email_starts_with_i = sgqlc.types.Field(String, graphql_name='email_starts_with_i')
    email_not_starts_with_i = sgqlc.types.Field(String, graphql_name='email_not_starts_with_i')
    email_ends_with_i = sgqlc.types.Field(String, graphql_name='email_ends_with_i')
    email_not_ends_with_i = sgqlc.types.Field(String, graphql_name='email_not_ends_with_i')
    email_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='email_in')
    email_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='email_not_in')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')
    is_admin_not = sgqlc.types.Field(Boolean, graphql_name='isAdmin_not')
    password_is_set = sgqlc.types.Field(Boolean, graphql_name='password_is_set')
    organization = sgqlc.types.Field(OrganizationWhereInput, graphql_name='organization')
    organization_is_null = sgqlc.types.Field(Boolean, graphql_name='organization_is_null')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    updated_at_not = sgqlc.types.Field(DateTime, graphql_name='updatedAt_not')
    updated_at_lt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lt')
    updated_at_lte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lte')
    updated_at_gt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gt')
    updated_at_gte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gte')
    updated_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_in')
    updated_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_not_in')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    created_at_not = sgqlc.types.Field(DateTime, graphql_name='createdAt_not')
    created_at_lt = sgqlc.types.Field(DateTime, graphql_name='createdAt_lt')
    created_at_lte = sgqlc.types.Field(DateTime, graphql_name='createdAt_lte')
    created_at_gt = sgqlc.types.Field(DateTime, graphql_name='createdAt_gt')
    created_at_gte = sgqlc.types.Field(DateTime, graphql_name='createdAt_gte')
    created_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_in')
    created_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_not_in')


class UserWhereUniqueInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class UsersCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(UserCreateInput, graphql_name='data')


class UsersUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id', 'data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    data = sgqlc.types.Field(UserUpdateInput, graphql_name='data')


class WidgetCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name', 'organization', 'language', 'sources')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization = sgqlc.types.Field(OrganizationRelateToOneInput, graphql_name='organization')
    language = sgqlc.types.Field(LanguageRelateToOneInput, graphql_name='language')
    sources = sgqlc.types.Field(SourceRelateToManyInput, graphql_name='sources')


class WidgetUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('name', 'organization', 'language', 'sources')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization = sgqlc.types.Field(OrganizationRelateToOneInput, graphql_name='organization')
    language = sgqlc.types.Field(LanguageRelateToOneInput, graphql_name='language')
    sources = sgqlc.types.Field(SourceRelateToManyInput, graphql_name='sources')


class WidgetWhereInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = (
        'and_', 'or_', 'id', 'id_not', 'id_in', 'id_not_in', 'name', 'name_not', 'name_contains', 'name_not_contains',
        'name_starts_with', 'name_not_starts_with', 'name_ends_with', 'name_not_ends_with', 'name_i', 'name_not_i',
        'name_contains_i', 'name_not_contains_i', 'name_starts_with_i', 'name_not_starts_with_i', 'name_ends_with_i',
        'name_not_ends_with_i', 'name_in', 'name_not_in', 'organization', 'organization_is_null', 'language',
        'language_is_null', 'sources_every', 'sources_some', 'sources_none', 'updated_at', 'updated_at_not',
        'updated_at_lt', 'updated_at_lte', 'updated_at_gt', 'updated_at_gte', 'updated_at_in', 'updated_at_not_in',
        'created_at', 'created_at_not', 'created_at_lt', 'created_at_lte', 'created_at_gt', 'created_at_gte',
        'created_at_in', 'created_at_not_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('WidgetWhereInput'), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('WidgetWhereInput'), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='id_not_in')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_i = sgqlc.types.Field(String, graphql_name='name_i')
    name_not_i = sgqlc.types.Field(String, graphql_name='name_not_i')
    name_contains_i = sgqlc.types.Field(String, graphql_name='name_contains_i')
    name_not_contains_i = sgqlc.types.Field(String, graphql_name='name_not_contains_i')
    name_starts_with_i = sgqlc.types.Field(String, graphql_name='name_starts_with_i')
    name_not_starts_with_i = sgqlc.types.Field(String, graphql_name='name_not_starts_with_i')
    name_ends_with_i = sgqlc.types.Field(String, graphql_name='name_ends_with_i')
    name_not_ends_with_i = sgqlc.types.Field(String, graphql_name='name_not_ends_with_i')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name_not_in')
    organization = sgqlc.types.Field(OrganizationWhereInput, graphql_name='organization')
    organization_is_null = sgqlc.types.Field(Boolean, graphql_name='organization_is_null')
    language = sgqlc.types.Field(LanguageWhereInput, graphql_name='language')
    language_is_null = sgqlc.types.Field(Boolean, graphql_name='language_is_null')
    sources_every = sgqlc.types.Field(SourceWhereInput, graphql_name='sources_every')
    sources_some = sgqlc.types.Field(SourceWhereInput, graphql_name='sources_some')
    sources_none = sgqlc.types.Field(SourceWhereInput, graphql_name='sources_none')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    updated_at_not = sgqlc.types.Field(DateTime, graphql_name='updatedAt_not')
    updated_at_lt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lt')
    updated_at_lte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_lte')
    updated_at_gt = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gt')
    updated_at_gte = sgqlc.types.Field(DateTime, graphql_name='updatedAt_gte')
    updated_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_in')
    updated_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='updatedAt_not_in')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    created_at_not = sgqlc.types.Field(DateTime, graphql_name='createdAt_not')
    created_at_lt = sgqlc.types.Field(DateTime, graphql_name='createdAt_lt')
    created_at_lte = sgqlc.types.Field(DateTime, graphql_name='createdAt_lte')
    created_at_gt = sgqlc.types.Field(DateTime, graphql_name='createdAt_gt')
    created_at_gte = sgqlc.types.Field(DateTime, graphql_name='createdAt_gte')
    created_at_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_in')
    created_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='createdAt_not_in')


class WidgetWhereUniqueInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class WidgetsCreateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(WidgetCreateInput, graphql_name='data')


class WidgetsUpdateInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('id', 'data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    data = sgqlc.types.Field(WidgetUpdateInput, graphql_name='data')


class _ListSchemaFieldsInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('type',)
    type = sgqlc.types.Field(String, graphql_name='type')


class _ksListsMetaInput(sgqlc.types.Input):
    __schema__ = coverified_schema
    __field_names__ = ('key', 'auxiliary')
    key = sgqlc.types.Field(String, graphql_name='key')
    auxiliary = sgqlc.types.Field(Boolean, graphql_name='auxiliary')


########################################################################
# Output Objects and Interfaces
########################################################################
class CloudinaryImage_File(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = (
        'id', 'path', 'filename', 'original_filename', 'mimetype', 'encoding', 'public_url', 'public_url_transformed')
    id = sgqlc.types.Field(ID, graphql_name='id')
    path = sgqlc.types.Field(String, graphql_name='path')
    filename = sgqlc.types.Field(String, graphql_name='filename')
    original_filename = sgqlc.types.Field(String, graphql_name='originalFilename')
    mimetype = sgqlc.types.Field(String, graphql_name='mimetype')
    encoding = sgqlc.types.Field(String, graphql_name='encoding')
    public_url = sgqlc.types.Field(String, graphql_name='publicUrl')
    public_url_transformed = sgqlc.types.Field(String, graphql_name='publicUrlTransformed', args=sgqlc.types.ArgDict((
        ('transformation', sgqlc.types.Arg(CloudinaryImageFormat, graphql_name='transformation', default=None)),
    ))
                                               )


class Entry(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = (
        '_label_', 'id', 'publish_date', 'title', 'image', 'content', 'url', 'tags', '_tags_meta', 'language', 'source',
        'updated_at', 'created_at')
    _label_ = sgqlc.types.Field(String, graphql_name='_label_')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    publish_date = sgqlc.types.Field(String, graphql_name='publishDate')
    title = sgqlc.types.Field(String, graphql_name='title')
    image = sgqlc.types.Field(CloudinaryImage_File, graphql_name='image')
    content = sgqlc.types.Field(String, graphql_name='content')
    url = sgqlc.types.Field(String, graphql_name='url')
    tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Tag'))),
                             graphql_name='tags', args=sgqlc.types.ArgDict((
            ('where', sgqlc.types.Arg(TagWhereInput, graphql_name='where', default=None)),
            ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
            ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortTagsBy)), graphql_name='sortBy',
                                        default=None)),
            ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
            ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
            ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ))
                             )
    _tags_meta = sgqlc.types.Field('_QueryMeta', graphql_name='_tagsMeta', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(TagWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by',
         sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortTagsBy)), graphql_name='sortBy', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                   )
    language = sgqlc.types.Field('Language', graphql_name='language')
    source = sgqlc.types.Field('Source', graphql_name='source')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')


class GeoLocation(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('_label_', 'id', 'name', 'location', 'radius', 'updated_at', 'created_at')
    _label_ = sgqlc.types.Field(String, graphql_name='_label_')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    location = sgqlc.types.Field('LocationGoogle', graphql_name='location')
    radius = sgqlc.types.Field(Float, graphql_name='radius')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')


class Language(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('_label_', 'id', 'name', 'updated_at', 'created_at')
    _label_ = sgqlc.types.Field(String, graphql_name='_label_')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')


class LocationGoogle(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('id', 'google_place_id', 'formatted_address', 'lat', 'lng')
    id = sgqlc.types.Field(ID, graphql_name='id')
    google_place_id = sgqlc.types.Field(String, graphql_name='googlePlaceID')
    formatted_address = sgqlc.types.Field(String, graphql_name='formattedAddress')
    lat = sgqlc.types.Field(Float, graphql_name='lat')
    lng = sgqlc.types.Field(Float, graphql_name='lng')


class Mutation(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = (
        'create_organization', 'create_organizations', 'update_organization', 'update_organizations',
        'delete_organization',
        'delete_organizations', 'create_tag', 'create_tags', 'update_tag', 'update_tags', 'delete_tag', 'delete_tags',
        'create_language', 'create_languages', 'update_language', 'update_languages', 'delete_language',
        'delete_languages',
        'create_geo_location', 'create_geo_locations', 'update_geo_location', 'update_geo_locations',
        'delete_geo_location',
        'delete_geo_locations', 'create_source', 'create_sources', 'update_source', 'update_sources', 'delete_source',
        'delete_sources', 'create_widget', 'create_widgets', 'update_widget', 'update_widgets', 'delete_widget',
        'delete_widgets', 'create_entry', 'create_entries', 'update_entry', 'update_entries', 'delete_entry',
        'delete_entries', 'create_user', 'create_users', 'update_user', 'update_users', 'delete_user', 'delete_users',
        'authenticate_user_with_password', 'unauthenticate_user', 'update_authenticated_user')
    create_organization = sgqlc.types.Field('Organization', graphql_name='createOrganization',
                                            args=sgqlc.types.ArgDict((
                                                ('data', sgqlc.types.Arg(OrganizationCreateInput, graphql_name='data',
                                                                         default=None)),
                                            ))
                                            )
    create_organizations = sgqlc.types.Field(sgqlc.types.list_of('Organization'), graphql_name='createOrganizations',
                                             args=sgqlc.types.ArgDict((
                                                 ('data', sgqlc.types.Arg(sgqlc.types.list_of(OrganizationsCreateInput),
                                                                          graphql_name='data', default=None)),
                                             ))
                                             )
    update_organization = sgqlc.types.Field('Organization', graphql_name='updateOrganization',
                                            args=sgqlc.types.ArgDict((
                                                ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id',
                                                                       default=None)),
                                                ('data', sgqlc.types.Arg(OrganizationUpdateInput, graphql_name='data',
                                                                         default=None)),
                                            ))
                                            )
    update_organizations = sgqlc.types.Field(sgqlc.types.list_of('Organization'), graphql_name='updateOrganizations',
                                             args=sgqlc.types.ArgDict((
                                                 ('data', sgqlc.types.Arg(sgqlc.types.list_of(OrganizationsUpdateInput),
                                                                          graphql_name='data', default=None)),
                                             ))
                                             )
    delete_organization = sgqlc.types.Field('Organization', graphql_name='deleteOrganization',
                                            args=sgqlc.types.ArgDict((
                                                ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id',
                                                                       default=None)),
                                            ))
                                            )
    delete_organizations = sgqlc.types.Field(sgqlc.types.list_of('Organization'), graphql_name='deleteOrganizations',
                                             args=sgqlc.types.ArgDict((
                                                 ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                                                                         graphql_name='ids', default=None)),
                                             ))
                                             )
    create_tag = sgqlc.types.Field('Tag', graphql_name='createTag', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(TagCreateInput, graphql_name='data', default=None)),
    ))
                                   )
    create_tags = sgqlc.types.Field(sgqlc.types.list_of('Tag'), graphql_name='createTags', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.list_of(TagsCreateInput), graphql_name='data', default=None)),
    ))
                                    )
    update_tag = sgqlc.types.Field('Tag', graphql_name='updateTag', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('data', sgqlc.types.Arg(TagUpdateInput, graphql_name='data', default=None)),
    ))
                                   )
    update_tags = sgqlc.types.Field(sgqlc.types.list_of('Tag'), graphql_name='updateTags', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.list_of(TagsUpdateInput), graphql_name='data', default=None)),
    ))
                                    )
    delete_tag = sgqlc.types.Field('Tag', graphql_name='deleteTag', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
    ))
                                   )
    delete_tags = sgqlc.types.Field(sgqlc.types.list_of('Tag'), graphql_name='deleteTags', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
    ))
                                    )
    create_language = sgqlc.types.Field(Language, graphql_name='createLanguage', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(LanguageCreateInput, graphql_name='data', default=None)),
    ))
                                        )
    create_languages = sgqlc.types.Field(sgqlc.types.list_of(Language), graphql_name='createLanguages',
                                         args=sgqlc.types.ArgDict((
                                             ('data', sgqlc.types.Arg(sgqlc.types.list_of(LanguagesCreateInput),
                                                                      graphql_name='data', default=None)),
                                         ))
                                         )
    update_language = sgqlc.types.Field(Language, graphql_name='updateLanguage', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('data', sgqlc.types.Arg(LanguageUpdateInput, graphql_name='data', default=None)),
    ))
                                        )
    update_languages = sgqlc.types.Field(sgqlc.types.list_of(Language), graphql_name='updateLanguages',
                                         args=sgqlc.types.ArgDict((
                                             ('data', sgqlc.types.Arg(sgqlc.types.list_of(LanguagesUpdateInput),
                                                                      graphql_name='data', default=None)),
                                         ))
                                         )
    delete_language = sgqlc.types.Field(Language, graphql_name='deleteLanguage', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
    ))
                                        )
    delete_languages = sgqlc.types.Field(sgqlc.types.list_of(Language), graphql_name='deleteLanguages',
                                         args=sgqlc.types.ArgDict((
                                             ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                                                                     graphql_name='ids', default=None)),
                                         ))
                                         )
    create_geo_location = sgqlc.types.Field(GeoLocation, graphql_name='createGeoLocation', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(GeoLocationCreateInput, graphql_name='data', default=None)),
    ))
                                            )
    create_geo_locations = sgqlc.types.Field(sgqlc.types.list_of(GeoLocation), graphql_name='createGeoLocations',
                                             args=sgqlc.types.ArgDict((
                                                 ('data', sgqlc.types.Arg(sgqlc.types.list_of(GeoLocationsCreateInput),
                                                                          graphql_name='data', default=None)),
                                             ))
                                             )
    update_geo_location = sgqlc.types.Field(GeoLocation, graphql_name='updateGeoLocation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('data', sgqlc.types.Arg(GeoLocationUpdateInput, graphql_name='data', default=None)),
    ))
                                            )
    update_geo_locations = sgqlc.types.Field(sgqlc.types.list_of(GeoLocation), graphql_name='updateGeoLocations',
                                             args=sgqlc.types.ArgDict((
                                                 ('data', sgqlc.types.Arg(sgqlc.types.list_of(GeoLocationsUpdateInput),
                                                                          graphql_name='data', default=None)),
                                             ))
                                             )
    delete_geo_location = sgqlc.types.Field(GeoLocation, graphql_name='deleteGeoLocation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
    ))
                                            )
    delete_geo_locations = sgqlc.types.Field(sgqlc.types.list_of(GeoLocation), graphql_name='deleteGeoLocations',
                                             args=sgqlc.types.ArgDict((
                                                 ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                                                                         graphql_name='ids', default=None)),
                                             ))
                                             )
    create_source = sgqlc.types.Field('Source', graphql_name='createSource', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(SourceCreateInput, graphql_name='data', default=None)),
    ))
                                      )
    create_sources = sgqlc.types.Field(sgqlc.types.list_of('Source'), graphql_name='createSources',
                                       args=sgqlc.types.ArgDict((
                                           ('data', sgqlc.types.Arg(sgqlc.types.list_of(SourcesCreateInput),
                                                                    graphql_name='data', default=None)),
                                       ))
                                       )
    update_source = sgqlc.types.Field('Source', graphql_name='updateSource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('data', sgqlc.types.Arg(SourceUpdateInput, graphql_name='data', default=None)),
    ))
                                      )
    update_sources = sgqlc.types.Field(sgqlc.types.list_of('Source'), graphql_name='updateSources',
                                       args=sgqlc.types.ArgDict((
                                           ('data', sgqlc.types.Arg(sgqlc.types.list_of(SourcesUpdateInput),
                                                                    graphql_name='data', default=None)),
                                       ))
                                       )
    delete_source = sgqlc.types.Field('Source', graphql_name='deleteSource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
    ))
                                      )
    delete_sources = sgqlc.types.Field(sgqlc.types.list_of('Source'), graphql_name='deleteSources',
                                       args=sgqlc.types.ArgDict((
                                           ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                                                                   graphql_name='ids', default=None)),
                                       ))
                                       )
    create_widget = sgqlc.types.Field('Widget', graphql_name='createWidget', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(WidgetCreateInput, graphql_name='data', default=None)),
    ))
                                      )
    create_widgets = sgqlc.types.Field(sgqlc.types.list_of('Widget'), graphql_name='createWidgets',
                                       args=sgqlc.types.ArgDict((
                                           ('data', sgqlc.types.Arg(sgqlc.types.list_of(WidgetsCreateInput),
                                                                    graphql_name='data', default=None)),
                                       ))
                                       )
    update_widget = sgqlc.types.Field('Widget', graphql_name='updateWidget', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('data', sgqlc.types.Arg(WidgetUpdateInput, graphql_name='data', default=None)),
    ))
                                      )
    update_widgets = sgqlc.types.Field(sgqlc.types.list_of('Widget'), graphql_name='updateWidgets',
                                       args=sgqlc.types.ArgDict((
                                           ('data', sgqlc.types.Arg(sgqlc.types.list_of(WidgetsUpdateInput),
                                                                    graphql_name='data', default=None)),
                                       ))
                                       )
    delete_widget = sgqlc.types.Field('Widget', graphql_name='deleteWidget', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
    ))
                                      )
    delete_widgets = sgqlc.types.Field(sgqlc.types.list_of('Widget'), graphql_name='deleteWidgets',
                                       args=sgqlc.types.ArgDict((
                                           ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                                                                   graphql_name='ids', default=None)),
                                       ))
                                       )
    create_entry = sgqlc.types.Field(Entry, graphql_name='createEntry', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(EntryCreateInput, graphql_name='data', default=None)),
    ))
                                     )
    create_entries = sgqlc.types.Field(sgqlc.types.list_of(Entry), graphql_name='createEntries',
                                       args=sgqlc.types.ArgDict((
                                           ('data', sgqlc.types.Arg(sgqlc.types.list_of(EntriesCreateInput),
                                                                    graphql_name='data', default=None)),
                                       ))
                                       )
    update_entry = sgqlc.types.Field(Entry, graphql_name='updateEntry', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('data', sgqlc.types.Arg(EntryUpdateInput, graphql_name='data', default=None)),
    ))
                                     )
    update_entries = sgqlc.types.Field(sgqlc.types.list_of(Entry), graphql_name='updateEntries',
                                       args=sgqlc.types.ArgDict((
                                           ('data', sgqlc.types.Arg(sgqlc.types.list_of(EntriesUpdateInput),
                                                                    graphql_name='data', default=None)),
                                       ))
                                       )
    delete_entry = sgqlc.types.Field(Entry, graphql_name='deleteEntry', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
    ))
                                     )
    delete_entries = sgqlc.types.Field(sgqlc.types.list_of(Entry), graphql_name='deleteEntries',
                                       args=sgqlc.types.ArgDict((
                                           ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                                                                   graphql_name='ids', default=None)),
                                       ))
                                       )
    create_user = sgqlc.types.Field('User', graphql_name='createUser', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(UserCreateInput, graphql_name='data', default=None)),
    ))
                                    )
    create_users = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='createUsers', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.list_of(UsersCreateInput), graphql_name='data', default=None)),
    ))
                                     )
    update_user = sgqlc.types.Field('User', graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('data', sgqlc.types.Arg(UserUpdateInput, graphql_name='data', default=None)),
    ))
                                    )
    update_users = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='updateUsers', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.list_of(UsersUpdateInput), graphql_name='data', default=None)),
    ))
                                     )
    delete_user = sgqlc.types.Field('User', graphql_name='deleteUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
    ))
                                    )
    delete_users = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='deleteUsers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
    ))
                                     )
    authenticate_user_with_password = sgqlc.types.Field('authenticateUserOutput',
                                                        graphql_name='authenticateUserWithPassword',
                                                        args=sgqlc.types.ArgDict((
                                                            ('email', sgqlc.types.Arg(String, graphql_name='email',
                                                                                      default=None)),
                                                            ('password',
                                                             sgqlc.types.Arg(String, graphql_name='password',
                                                                             default=None)),
                                                        ))
                                                        )
    unauthenticate_user = sgqlc.types.Field('unauthenticateUserOutput', graphql_name='unauthenticateUser')
    update_authenticated_user = sgqlc.types.Field('User', graphql_name='updateAuthenticatedUser',
                                                  args=sgqlc.types.ArgDict((
                                                      ('data', sgqlc.types.Arg(UserUpdateInput, graphql_name='data',
                                                                               default=None)),
                                                  ))
                                                  )


class Organization(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('_label_', 'id', 'name', 'updated_at', 'created_at')
    _label_ = sgqlc.types.Field(String, graphql_name='_label_')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')


class Query(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = (
        'all_organizations', 'organization', '_all_organizations_meta', 'all_tags', 'tag',
        '_all_tags_meta', 'all_languages', 'language', '_all_languages_meta',
        'all_geo_locations', 'geo_location', '_all_geo_locations_meta', 'all_sources', 'source',
        '_all_sources_meta', 'all_widgets', 'widget', '_all_widgets_meta',
        'all_entries', 'entry', '_all_entries_meta', 'all_users', 'user', '_all_users_meta', '_ks_lists_meta',
        'app_version', 'authenticated_user')
    all_organizations = sgqlc.types.Field(sgqlc.types.list_of('Organization'), graphql_name='allOrganizations',
                                          args=sgqlc.types.ArgDict((
                                              ('where', sgqlc.types.Arg(OrganizationWhereInput, graphql_name='where',
                                                                        default=None)),
                                              ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
                                              ('sort_by', sgqlc.types.Arg(
                                                  sgqlc.types.list_of(sgqlc.types.non_null(SortOrganizationsBy)),
                                                  graphql_name='sortBy', default=None)),
                                              ('order_by',
                                               sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
                                              ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
                                              ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
                                          ))
                                          )
    organization = sgqlc.types.Field('Organization', graphql_name='Organization', args=sgqlc.types.ArgDict((
        ('where',
         sgqlc.types.Arg(sgqlc.types.non_null(OrganizationWhereUniqueInput), graphql_name='where', default=None)),
    ))
                                     )
    _all_organizations_meta = sgqlc.types.Field('_QueryMeta', graphql_name='_allOrganizationsMeta',
                                                args=sgqlc.types.ArgDict((
                                                    ('where',
                                                     sgqlc.types.Arg(OrganizationWhereInput, graphql_name='where',
                                                                     default=None)),
                                                    ('search',
                                                     sgqlc.types.Arg(String, graphql_name='search', default=None)),
                                                    ('sort_by', sgqlc.types.Arg(
                                                        sgqlc.types.list_of(sgqlc.types.non_null(SortOrganizationsBy)),
                                                        graphql_name='sortBy', default=None)),
                                                    ('order_by',
                                                     sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
                                                    ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
                                                    ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
                                                ))
                                                )
    __organizations_meta = sgqlc.types.Field('_ListMeta', graphql_name='_OrganizationsMeta')
    all_tags = sgqlc.types.Field(sgqlc.types.list_of('Tag'), graphql_name='allTags', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(TagWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by',
         sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortTagsBy)), graphql_name='sortBy', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                 )
    tag = sgqlc.types.Field('Tag', graphql_name='Tag', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(TagWhereUniqueInput), graphql_name='where', default=None)),
    ))
                            )
    _all_tags_meta = sgqlc.types.Field('_QueryMeta', graphql_name='_allTagsMeta', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(TagWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by',
         sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortTagsBy)), graphql_name='sortBy', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                       )
    __tags_meta = sgqlc.types.Field('_ListMeta', graphql_name='_TagsMeta')
    all_languages = sgqlc.types.Field(sgqlc.types.list_of('Language'), graphql_name='allLanguages',
                                      args=sgqlc.types.ArgDict((
                                          ('where',
                                           sgqlc.types.Arg(LanguageWhereInput, graphql_name='where', default=None)),
                                          ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
                                          ('sort_by',
                                           sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortLanguagesBy)),
                                                           graphql_name='sortBy', default=None)),
                                          ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
                                          ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
                                          ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
                                      ))
                                      )
    language = sgqlc.types.Field('Language', graphql_name='Language', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(LanguageWhereUniqueInput), graphql_name='where', default=None)),
    ))
                                 )
    _all_languages_meta = sgqlc.types.Field('_QueryMeta', graphql_name='_allLanguagesMeta', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(LanguageWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortLanguagesBy)), graphql_name='sortBy',
                                    default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                            )
    __languages_meta = sgqlc.types.Field('_ListMeta', graphql_name='_LanguagesMeta')
    all_geo_locations = sgqlc.types.Field(sgqlc.types.list_of('GeoLocation'), graphql_name='allGeoLocations',
                                          args=sgqlc.types.ArgDict((
                                              ('where', sgqlc.types.Arg(GeoLocationWhereInput, graphql_name='where',
                                                                        default=None)),
                                              ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
                                              ('sort_by', sgqlc.types.Arg(
                                                  sgqlc.types.list_of(sgqlc.types.non_null(SortGeoLocationsBy)),
                                                  graphql_name='sortBy', default=None)),
                                              ('order_by',
                                               sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
                                              ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
                                              ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
                                          ))
                                          )
    geo_location = sgqlc.types.Field('GeoLocation', graphql_name='GeoLocation', args=sgqlc.types.ArgDict((
        ('where',
         sgqlc.types.Arg(sgqlc.types.non_null(GeoLocationWhereUniqueInput), graphql_name='where', default=None)),
    ))
                                     )
    _all_geo_locations_meta = sgqlc.types.Field('_QueryMeta', graphql_name='_allGeoLocationsMeta',
                                                args=sgqlc.types.ArgDict((
                                                    ('where',
                                                     sgqlc.types.Arg(GeoLocationWhereInput, graphql_name='where',
                                                                     default=None)),
                                                    ('search',
                                                     sgqlc.types.Arg(String, graphql_name='search', default=None)),
                                                    ('sort_by', sgqlc.types.Arg(
                                                        sgqlc.types.list_of(sgqlc.types.non_null(SortGeoLocationsBy)),
                                                        graphql_name='sortBy', default=None)),
                                                    ('order_by',
                                                     sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
                                                    ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
                                                    ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
                                                ))
                                                )
    __geo_locations_meta = sgqlc.types.Field('_ListMeta', graphql_name='_GeoLocationsMeta')
    all_sources = sgqlc.types.Field(sgqlc.types.list_of('Source'), graphql_name='allSources', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(SourceWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortSourcesBy)), graphql_name='sortBy',
                                    default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                    )
    source = sgqlc.types.Field('Source', graphql_name='Source', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(SourceWhereUniqueInput), graphql_name='where', default=None)),
    ))
                               )
    _all_sources_meta = sgqlc.types.Field('_QueryMeta', graphql_name='_allSourcesMeta', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(SourceWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortSourcesBy)), graphql_name='sortBy',
                                    default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                          )
    __sources_meta = sgqlc.types.Field('_ListMeta', graphql_name='_SourcesMeta')
    all_widgets = sgqlc.types.Field(sgqlc.types.list_of('Widget'), graphql_name='allWidgets', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(WidgetWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortWidgetsBy)), graphql_name='sortBy',
                                    default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                    )
    widget = sgqlc.types.Field('Widget', graphql_name='Widget', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(WidgetWhereUniqueInput), graphql_name='where', default=None)),
    ))
                               )
    _all_widgets_meta = sgqlc.types.Field('_QueryMeta', graphql_name='_allWidgetsMeta', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(WidgetWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortWidgetsBy)), graphql_name='sortBy',
                                    default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                          )
    __widgets_meta = sgqlc.types.Field('_ListMeta', graphql_name='_WidgetsMeta')
    all_entries = sgqlc.types.Field(sgqlc.types.list_of('Entry'), graphql_name='allEntries', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(EntryWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortEntriesBy)), graphql_name='sortBy',
                                    default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                    )
    entry = sgqlc.types.Field('Entry', graphql_name='Entry', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(EntryWhereUniqueInput), graphql_name='where', default=None)),
    ))
                              )
    _all_entries_meta = sgqlc.types.Field('_QueryMeta', graphql_name='_allEntriesMeta', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(EntryWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortEntriesBy)), graphql_name='sortBy',
                                    default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                          )
    __entries_meta = sgqlc.types.Field('_ListMeta', graphql_name='_EntriesMeta')
    all_users = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='allUsers', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(UserWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by',
         sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortUsersBy)), graphql_name='sortBy', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                  )
    user = sgqlc.types.Field('User', graphql_name='User', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(sgqlc.types.non_null(UserWhereUniqueInput), graphql_name='where', default=None)),
    ))
                             )
    _all_users_meta = sgqlc.types.Field('_QueryMeta', graphql_name='_allUsersMeta', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(UserWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by',
         sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortUsersBy)), graphql_name='sortBy', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                        )
    __users_meta = sgqlc.types.Field('_ListMeta', graphql_name='_UsersMeta')
    _ks_lists_meta = sgqlc.types.Field(sgqlc.types.list_of('_ListMeta'), graphql_name='_ksListsMeta',
                                       args=sgqlc.types.ArgDict((
                                           ('where',
                                            sgqlc.types.Arg(_ksListsMetaInput, graphql_name='where', default=None)),
                                       ))
                                       )
    app_version = sgqlc.types.Field(String, graphql_name='appVersion')
    authenticated_user = sgqlc.types.Field('User', graphql_name='authenticatedUser')


class Source(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('_label_', 'id', 'name', 'url', 'location', 'description', 'updated_at', 'created_at')
    _label_ = sgqlc.types.Field(String, graphql_name='_label_')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    url = sgqlc.types.Field(String, graphql_name='url')
    location = sgqlc.types.Field(GeoLocation, graphql_name='location')
    description = sgqlc.types.Field(String, graphql_name='description')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')


class Tag(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = (
        '_label_', 'id', 'name', 'language', 'description', 'relevance', 'image', 'updated_at', 'created_at')
    _label_ = sgqlc.types.Field(String, graphql_name='_label_')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    language = sgqlc.types.Field(Language, graphql_name='language')
    description = sgqlc.types.Field(String, graphql_name='description')
    relevance = sgqlc.types.Field(Int, graphql_name='relevance')
    image = sgqlc.types.Field(CloudinaryImage_File, graphql_name='image')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')


class User(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = (
        '_label_', 'id', 'name', 'email', 'is_admin', 'password_is_set', 'organization', 'updated_at', 'created_at')
    _label_ = sgqlc.types.Field(String, graphql_name='_label_')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    email = sgqlc.types.Field(String, graphql_name='email')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')
    password_is_set = sgqlc.types.Field(Boolean, graphql_name='password_is_set')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')


class Widget(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = (
        '_label_', 'id', 'name', 'organization', 'language', 'sources', '_sources_meta', 'updated_at', 'created_at')
    _label_ = sgqlc.types.Field(String, graphql_name='_label_')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    language = sgqlc.types.Field(Language, graphql_name='language')
    sources = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Source))),
                                graphql_name='sources', args=sgqlc.types.ArgDict((
            ('where', sgqlc.types.Arg(SourceWhereInput, graphql_name='where', default=None)),
            ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
            ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortSourcesBy)), graphql_name='sortBy',
                                        default=None)),
            ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
            ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
            ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ))
                                )
    _sources_meta = sgqlc.types.Field('_QueryMeta', graphql_name='_sourcesMeta', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(SourceWhereInput, graphql_name='where', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SortSourcesBy)), graphql_name='sortBy',
                                    default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
    ))
                                      )
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')


class _ListAccess(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('create', 'read', 'update', 'delete', 'auth')
    create = sgqlc.types.Field(Boolean, graphql_name='create')
    read = sgqlc.types.Field(JSON, graphql_name='read')
    update = sgqlc.types.Field(JSON, graphql_name='update')
    delete = sgqlc.types.Field(JSON, graphql_name='delete')
    auth = sgqlc.types.Field(JSON, graphql_name='auth')


class _ListInputTypes(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = (
        'where_input', 'where_unique_input', 'create_input', 'create_many_input', 'update_input', 'update_many_input')
    where_input = sgqlc.types.Field(String, graphql_name='whereInput')
    where_unique_input = sgqlc.types.Field(String, graphql_name='whereUniqueInput')
    create_input = sgqlc.types.Field(String, graphql_name='createInput')
    create_many_input = sgqlc.types.Field(String, graphql_name='createManyInput')
    update_input = sgqlc.types.Field(String, graphql_name='updateInput')
    update_many_input = sgqlc.types.Field(String, graphql_name='updateManyInput')


class _ListMeta(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('key', 'description', 'label', 'singular', 'plural', 'path', 'access', 'schema')
    key = sgqlc.types.Field(String, graphql_name='key')
    description = sgqlc.types.Field(String, graphql_name='description')
    label = sgqlc.types.Field(String, graphql_name='label')
    singular = sgqlc.types.Field(String, graphql_name='singular')
    plural = sgqlc.types.Field(String, graphql_name='plural')
    path = sgqlc.types.Field(String, graphql_name='path')
    access = sgqlc.types.Field(_ListAccess, graphql_name='access')
    schema = sgqlc.types.Field('_ListSchema', graphql_name='schema')


class _ListMutations(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('create', 'create_many', 'update', 'update_many', 'delete', 'delete_many')
    create = sgqlc.types.Field(String, graphql_name='create')
    create_many = sgqlc.types.Field(String, graphql_name='createMany')
    update = sgqlc.types.Field(String, graphql_name='update')
    update_many = sgqlc.types.Field(String, graphql_name='updateMany')
    delete = sgqlc.types.Field(String, graphql_name='delete')
    delete_many = sgqlc.types.Field(String, graphql_name='deleteMany')


class _ListQueries(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('item', 'list', 'meta')
    item = sgqlc.types.Field(String, graphql_name='item')
    list = sgqlc.types.Field(String, graphql_name='list')
    meta = sgqlc.types.Field(String, graphql_name='meta')


class _ListSchema(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('type', 'queries', 'mutations', 'input_types', 'fields', 'related_fields')
    type = sgqlc.types.Field(String, graphql_name='type')
    queries = sgqlc.types.Field(_ListQueries, graphql_name='queries')
    mutations = sgqlc.types.Field(_ListMutations, graphql_name='mutations')
    input_types = sgqlc.types.Field(_ListInputTypes, graphql_name='inputTypes')
    fields = sgqlc.types.Field(sgqlc.types.list_of('_ListSchemaFields'), graphql_name='fields',
                               args=sgqlc.types.ArgDict((
                                   ('where',
                                    sgqlc.types.Arg(_ListSchemaFieldsInput, graphql_name='where', default=None)),
                               ))
                               )
    related_fields = sgqlc.types.Field(sgqlc.types.list_of('_ListSchemaRelatedFields'), graphql_name='relatedFields')


class _ListSchemaFields(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('path', 'type')
    path = sgqlc.types.Field(String, graphql_name='path')
    type = sgqlc.types.Field(String, graphql_name='type')


class _ListSchemaRelatedFields(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('type', 'fields')
    type = sgqlc.types.Field(String, graphql_name='type')
    fields = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fields')


class _QueryMeta(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('count',)
    count = sgqlc.types.Field(Int, graphql_name='count')


class authenticateUserOutput(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('token', 'item')
    token = sgqlc.types.Field(String, graphql_name='token')
    item = sgqlc.types.Field(User, graphql_name='item')


class unauthenticateUserOutput(sgqlc.types.Type):
    __schema__ = coverified_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
coverified_schema.query_type = Query
coverified_schema.mutation_type = Mutation
coverified_schema.subscription_type = None
