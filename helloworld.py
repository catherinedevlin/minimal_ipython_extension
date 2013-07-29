from IPython.core.magic import Magics, magics_class, line_magic, cell_magic

#-----------------------------------------------------------------------------
# Functions and classes
#-----------------------------------------------------------------------------

@magics_class
class HelloWorldMagics(Magics):
    """A simple Hello, <name> magic.
    
    """

    @line_magic  # or call with ("hi") to make %hi the magic name
    @cell_magic  
    def helloworld(self, line='', cell=None):
        """Virtually empty magic for demonstration purposes.

        Example::
        
          In [1]: %load_ext helloworld

          In [2]: %helloworld Catherine
          Out[2]: u'Hello, Catherine'
        

        """
        return "Hello, %s\n%s" % (line, cell or "")
       
def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(HelloWorldMagics)
