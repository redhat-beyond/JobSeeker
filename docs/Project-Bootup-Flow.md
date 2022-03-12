# Project Boot-Up Flow

These graphs show visually the flow of the bootup process of the project once the client runs the `vagrant up` command.

- ## Boot-Up Structure
    ```mermaid
    flowchart TB
    subgraph Vagrant["Vagrant (With 'fedora/34-cloud-base' Running On VirtualBox)"]
        subgraph Pipenv
            subgraph Django[Django Application]
            end
        end
    end
    ```

- ## Boot-Up Flow
    ```mermaid
    flowchart TB
    Vagrant["Vagrant (With 'fedora/34-cloud-base' Running On VirtualBox)"]
    Pipenv
    Django

    Command["`vagrant up` command"] -->|Launches| Vagrant -->|Launches| Pipenv -->|Launches| Django[Django Application]
    ```
