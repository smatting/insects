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
    PocessId
    Timestamp

data BoundingBox =
  BoundingBox
    ProcessId
    BoundingBoxId
    Int -- ^ x
    Int -- ^ y
    Int -- ^ width
    Int -- ^ height

data Process =
  Process
    ProcessId

data ObjectTracking =
  ObjectTracking
    ObjectTrackingId
    ProcessId
    [AppearanceId]

data Appearance =
  Appearance
    AppearanceId
    ProcessId
    FrameId
    (Maybe BoundingBoxId)

data Class
  = Class
      ClassId
      Name

data Classification
  = AppearanceClassification
      ProcessId
      AppearanceId
      [(Float, ClassId)]
  | ObjectTrackingClassification 
      ProcessId
      ObjectTrackingId
      [(Float, ClassId)]

data Relation
  = Relation
      RelationId
      ([ClipId | AppearanceId | RelationId])
