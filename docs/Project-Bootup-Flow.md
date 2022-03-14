# Project Boot-Up Flow

These graphs visually show the flow of the bootup process of the project once the client runs the `vagrant up` command.

- ## Boot-Up Structure
    ```mermaid
    flowchart TB
    subgraph Vagrant["Vagrant (With 'fedora/34-cloud-base' Virtual Machine running in VirtualBox)"]
        subgraph Pipenv
            subgraph Django[Django Application]
            end
        end
    end
    ```

- ## Boot-Up Flow
    ```mermaid
    flowchart TB
    Vagrant["Vagrant (With 'fedora/34-cloud-base' Virtual Machine running in VirtualBox)"]
    Pipenv
    Django

    Command["`vagrant up` command"] -->|Launches| Vagrant -->|Launches| Pipenv -->|Launches| Django[Django Application]
    ```
