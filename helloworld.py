from IPython.core.magic import Magics, magics_class, line_magic

#-----------------------------------------------------------------------------
# Functions and classes
#-----------------------------------------------------------------------------

@magics_class
class HelloWorldMagics(Magics):
    """Lightweight persistence for python variables.

    Provides the %store magic."""

    #@skip_doctest
    @line_magic
    def helloworld(self, parameter_s=''):
        """Virtually empty magic for demonstration purposes.

        Example::
        
          In [1]: %load_ext helloworld

          In [2]: %helloworld Catherine
          Out[2]: u'Hello, Catherine'
        

       """

        opts,argsl = self.parse_options(parameter_s,'drz',mode='string')
        return "Hello, %s" % argsl
       
def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(HelloWorldMagics)
