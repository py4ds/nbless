from subprocess import call
import argparse


def render(input_name: str = 'unrendered.Rmd',
           input_path: str = './',
           output_format: str = 'NULL',
           output_name: str = 'NULL',
           output_path: str = 'NULL'
           #output_options: str = 'NULL',
           #interm_path: str = 'NULL',
           #knit_root_path: str = 'NULL',
           #runtime: str = 'c("auto", "static", "shiny", "shiny_prerendered")',
           #clean: str = 'TRUE',
           #params: str = 'NULL',
           #knit_meta: str = 'NULL',
           #envir: str = 'parent.frame()',
           #run_pandoc: str = 'TRUE',
           #quiet: str = 'FALSE'#,
           #encoding: str = 'getOption("encoding")'
           ) -> None:

    if not input_path.endswith('/'):
        input_path += '/'

    call(['Rscript -e rmarkdown::render('
           f'"{input_path+input_name}")']
           #f'output_format = "{output_format}", '
           #f'output_file = "{output_name}", '
           #f'output_dir = "{output_path}") '
           #f'output_options = "{output_options}", '
           #f'intermediates_dir = "{interm_path}", '
           #f'knit_root_dir = "{knit_root_path}", '
           #f'runtime = "{runtime}", '
           #f'clean = "{clean}", '
           #f'params = "{params}", '
           #f'knit_meta = "{knit_meta}", '
           #f'envir = "{envir}", '
           #f'run_pandoc = "{run_pandoc}", '
           #f'quiet = "{quiet}")'
           #f'encoding = "{encoding}")'
           )

def command_line_runner():

    parser = argparse.ArgumentParser(
        description='Create an R markdown file from the command line.')

    parser.add_argument('input_name',
                        help='The filename of the input Rmd file, '
                             'which can be R script, Rmd, or plain markdown.')

    parser.add_argument('--input_path', '-i', default='./',
                        help='The filepath to the input Rmd file.')

    parser.add_argument('--format', '-f', default='NULL',
                        help='The format of the rendered output file.')

    parser.add_argument('--output_name', '-n', default='NULL',
                        help='The filename of the rendered output file.')

    parser.add_argument('--output_path', '-p', default='NULL',
                        help='The filepath where the output file is saved.')

    #parser.add_argument('--output_options', '-o', default='NULL')
    #parser.add_argument('--interm_path', '-t', default='NULL')
    #parser.add_argument('--knit_root_path', '-k', default='NULL')
    #parser.add_argument('--runtime', '-r',
    #                    default='c("auto", '
    #                            '"static", "shiny", "shiny_prerendered")')
    #parser.add_argument('--clean', '-c', default='TRUE')
    #parser.add_argument('--params', '-a', default='NULL')
    #parser.add_argument('--knit_meta', '-m', default='NULL')
    #parser.add_argument('--envir', '-v', default='parent.frame()')
    #parser.add_argument('--run_pandoc', '-r', default='TRUE')
    #parser.add_argument('--quiet', '-q', default='FALSE')
    #parser.add_argument('--encoding', '-d', default='getOption("encoding")')

    args = parser.parse_args()

    input_name = args.input_name
    input_path = args.input_path
    output_format = args.format
    output_name = args.output_name
    output_path = args.output_path
    #output_options = args.output_options
    #interm_path = args.interm_path
    #knit_root_path = args.knit_root_path
    #runtime = args.runtime
    #clean = args.clean
    #params = args.params
    #knit_meta = args.knit_meta
    #envir = args.envir
    #run_pandoc = args.run_pandoc
    #quiet = args.quiet
    #encoding = args.encoding

    render(input_name = input_name,
           input_path = input_path,
           output_format = output_format,
           output_name = output_name,
           output_path = output_path
           #output_options = output_options,
           #interm_path = interm_path,
           #knit_root_path = knit_root_path,
           #runtime = runtime,
           #clean = clean,
           #params = params,
           #knit_meta = knit_meta,
           #envir = envir,
           #run_pandoc = run_pandoc,
           #quiet = quiet,
           #encoding = encoding
           )

if __name__ == "__main__":
    command_line_runner()
