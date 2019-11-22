module Structure
where


{-|

   This is how yo defined data types:

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

-}

-- | FrameIndex 0 = erster Frame
--   FrameIndex 1 = zweiter Frame
-- newtype FrameIndex = FrameIndex Int

data Frame =
  Frame
    FrameId
    Timestamp

data Clip =
  Clip
    ClipId
    [FrameId]

data BoundingBox =
  BoundingBox
    BoundingBoxId
    Int -- ^ x
    Int -- ^ y
    Int -- ^ width
    Int -- ^ height

data AnnotatedFrame =
  AnnotatedFrame
    AnnotatedFrameId
    FrameId
    [BoundingBoxId]

data Object =
  Object
    ObjectId

data ObjectTracking =
  ObjectTracking
    ObjectTrackingId
    ObjectId
    [(AnnotatedFrameId, BoundingBoxId)]
    (Maybe AnnCollectionId)

data AnnCollection =
  AnnCollection
    AnnCollectionId
    [(FrameId, AnnotatedFrame)] -- ^ At most 1 annotation per frame
    (Maybe ClipId) -- ^ Possible origin clip

data FrameId = FrameId Int
data ClipId = ClipId Int
data ObjectId = ObjectId Int
data BoundingBoxId = BoundingBoxId Int
data Timestamp = Timestamp Int
data AnnotatedFrameId = AnnotatedFrameId Int
data AnnCollectionId = AnnCollectionId Int
data ObjectTrackingId = ObjectTrackingId Int

