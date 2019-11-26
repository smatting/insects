module Structure
where


{-|

   This is how you define custom data types:

    data Person = Person Text Text
         ^        ^      ^    ^
         |        |      |    |
         |        |      |    type of 2nd field
         |        |      |
         |        |      type of 1st field
         |        |
         |        name of data constructor of the type,
         |        if type has only 1 constructur convetion is to
         |        use the same name as the type
         |
         name of type

    Other type constructors:

    - If "Foo" is a type, then "[Foo]" is the type "list of Foo"
    - If "Foo" is a type, then "Maybe Foo" is a type which has the same values as Foo
      plus a value "Nothing" which is the absence of a value, like "null" or "None"
    - If "Foo" and "Bar" are types then "(Foo, Bar)" is the type of tuples

-}


data Frame =
  Frame
    FrameId
    Timestamp

data BoundingBox =
  BoundingBox
    BoundingBoxId
    Int -- ^ x
    Int -- ^ y
    Int -- ^ width
    Int -- ^ height

data Appearance =
  Appearance
    AppearanceId
    FrameId
    (Maybe BoundingBoxId)

data Object =
  Object
    ObjectId
    [ObjectTag]
    [AppearanceId]

data ObjectTag =
  ObjectTag
    ObjectTagId
    TagName

data Collection =
  Collection
    CollectionId
    CollectionName
    [Object]

data FrameId = FrameId Int
data BoundingBoxId = BoundingBoxId Int
data ObjectId = ObjectId Int
data ObjectTagId = ObjectTagId Int
data Timestamp = Timestamp Int
data AppearanceId = AppearanceId Int
data CollectionId = CollectionId Int
