from __future__ import absolute_import
from __future__ import division
from __future__ import print_function



from inception.dataset import Dataset


class PlaceData(Dataset):
  """Place data set."""

  def __init__(self, subset):
    super(PlaceData, self).__init__('Place', subset)

  def num_classes(self):
    """Returns the number of classes in the data set."""
    return 205

  def num_examples_per_epoch(self):
    """Returns the number of examples in the data subset."""
    if self.subset == 'train':
      return 2448873
    if self.subset == 'validation':
      return 20500

  def download_message(self):
    """Instruction to download and extract the tarball from Flowers website."""

    print('Failed to find any Place %s files'% self.subset)
    print('')
    print('If you have already downloaded and processed the data, then make '
          'sure to set --data_dir to point to the directory containing the '
          'location of the sharded TFRecords.\n')
    print('If you have not downloaded and prepared the Place data in the '
          'TFRecord format, you will need to do this at least once. This '
          'process could take several hours depending on the speed of your '
          'computer and network connection\n')
    print('Please see README.md for instructions on how to build '
          'the Place dataset using data/build_image_data.py.\n')
    print('Note that the raw data size is 137 GB and the processed data size '
          'is 132 GB. Please ensure you have at least 300GB disk space.')
