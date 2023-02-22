## Oracle 3 Optimized Test Folder
### Makefile options:
<ul>
    <li> make all
    <ul>
        <li> First generates the "unparse.expected" files for every ".jeff" file in the immediate directory (my addition)
        <li> Then tests each ".jeff" file by printing the diff between your unparse output and the expected unparse ouput (if any)
    </ul>
    <li> make nogen
    <ul>
      <li> Just tests each ".jeff" file by printing the diff between your unparse output and the expected unparse ouput (if any)
      <li> (i.e. just runs the same test commands as the starter code)
</ul>
####
